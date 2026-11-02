import contextlib
import importlib.util
import io
import os
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location('bottest', Path(__file__).resolve().parents[1] / 'bottest.py')
recon = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(recon)


class ReconTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.output = Path(self.tmp.name) / 'results.txt'
        self.log = contextlib.redirect_stdout(io.StringIO())
        self.log.__enter__()
        self.addCleanup(self.log.__exit__, None, None, None)

    def test_full_domain_output_directories_are_distinct(self):
        self.assertEqual(recon.output_directory('example.com'), Path('recon_example.com'))
        self.assertNotEqual(recon.output_directory('example.com'), recon.output_directory('example.org'))

    def test_unmarked_partial_output_is_replaced(self):
        self.output.write_text('partial\n')
        calls = []
        def complete():
            calls.append(True)
            self.assertFalse(self.output.exists())
            self.output.write_text('complete\n')
            return True
        recon.skip_or_run(str(self.output), complete)
        self.assertEqual(calls, [True])
        self.assertEqual(self.output.read_text(), 'complete\n')

    def test_successful_empty_step_is_resumed(self):
        calls = []
        def complete():
            calls.append(True)
            return True
        recon.skip_or_run(str(self.output), complete)
        recon.skip_or_run(str(self.output), complete)
        self.assertEqual(calls, [True])

    def test_failed_step_is_not_completed(self):
        def fail():
            self.output.write_text('partial\n')
            return False
        with self.assertRaises(RuntimeError):
            recon.skip_or_run(str(self.output), fail)
        calls = []
        recon.skip_or_run(str(self.output), lambda: calls.append(True) or True)
        self.assertEqual(calls, [True])

    def test_interrupted_step_is_retried(self):
        def interrupt():
            self.output.write_text('partial\n')
            raise KeyboardInterrupt
        with self.assertRaises(KeyboardInterrupt):
            recon.skip_or_run(str(self.output), interrupt)
        calls = []
        recon.skip_or_run(str(self.output), lambda: calls.append(True) or True)
        self.assertEqual(calls, [True])

    def test_missing_companion_output_forces_rerun(self):
        companion = self.output.with_suffix('.json')
        calls = []
        def complete():
            calls.append(True)
            companion.write_text('{}\n')
            return True
        recon.skip_or_run(str(self.output), complete, extra_outputs=[str(companion)])
        companion.unlink()
        recon.skip_or_run(str(self.output), complete, extra_outputs=[str(companion)])
        self.assertEqual(calls, [True, True])

    def test_changed_input_forces_rerun(self):
        source = self.output.with_name('input.txt')
        source.write_text('first\n')
        calls = []
        complete = lambda: calls.append(True) or True
        recon.skip_or_run(str(self.output), complete, inputs=[str(source)])
        source.write_text('changed input\n')
        recon.skip_or_run(str(self.output), complete, inputs=[str(source)])
        self.assertEqual(calls, [True, True])


    def test_empty_upstream_clears_previous_downstream_results(self):
        source = self.output.with_name('input.txt')
        source.write_text('old input\n')
        def complete():
            self.output.write_text('old finding\n')
            return True
        recon.skip_or_run(str(self.output), complete, inputs=[str(source)])
        source.write_text('')
        recon.skip_or_run(str(self.output), lambda: self.fail('empty input must not run tools'), inputs=[str(source)])
        self.assertEqual(self.output.read_text(), '')

    def test_pipeline_upstream_failure_is_reported(self):
        self.assertFalse(recon.pipe('false | true'))

    def test_httpx_json_is_preserved_and_urls_are_parsed(self):
        source = self.output.with_name('ports.txt')
        source.write_text('example.com:443\n')
        records = self.output.with_suffix('.json')
        payload = '\n'.join([
            json.dumps({'url': 'https://example.com/a?x=1&y=2'}),
            json.dumps({'url': 'https://example.com/a?x=1&y=2'}),
            json.dumps({'url': 'https://example.com/escaped"path'}),
            json.dumps({'title': 'no url'}),
        ]) + '\n'
        def fake_run(cmd, **kwargs):
            self.assertEqual(cmd, ['httpx', '-silent', '-json', '-l', str(source)])
            kwargs['stdout'].write(payload)
            return subprocess.CompletedProcess(cmd, 0)
        with patch.object(recon.subprocess, 'run', side_effect=fake_run):
            self.assertTrue(recon.probe_http(str(source), str(self.output), str(records)))
        self.assertEqual(records.read_text(), payload)
        self.assertEqual(self.output.read_text().splitlines(), [
            'https://example.com/a?x=1&y=2', 'https://example.com/escaped"path',
        ])

    def test_httpx_failure_prevents_parsing_partial_results(self):
        records = self.output.with_suffix('.json')
        with patch.object(recon.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1)):
            self.assertFalse(recon.probe_http('ports.txt', str(self.output), str(records)))
        self.assertFalse(self.output.exists())

    def test_malformed_httpx_json_does_not_complete_step(self):
        records = self.output.with_suffix('.json')
        def fake_run(cmd, **kwargs):
            kwargs['stdout'].write('not json\n')
            return subprocess.CompletedProcess(cmd, 0)
        with patch.object(recon.subprocess, 'run', side_effect=fake_run):
            with self.assertRaises(ValueError):
                recon.probe_http('ports.txt', str(self.output), str(records))

    def test_xss_candidates_remain_deduplicated(self):
        source = self.output.with_name('urls.txt')
        source.write_text('https://example.com/?a=1\n')
        duplicate = 'https://example.com/?a=1\n' * 2
        with patch.object(recon.subprocess, 'run', return_value=subprocess.CompletedProcess([], 0, duplicate, '')):
            self.assertTrue(recon.extract_xss(str(source), str(self.output)))
        self.assertEqual(self.output.read_text(), 'https://example.com/?a=1\n')

    def test_gf_no_matches_is_success_but_errors_are_not(self):
        source = self.output.with_name('urls.txt')
        source.write_text('https://example.com/\n')
        with patch.object(recon.subprocess, 'run', return_value=subprocess.CompletedProcess([], 1, '', '')):
            self.assertTrue(recon.extract_xss(str(source), str(self.output)))
        for status in [0, 1]:
            with patch.object(recon.subprocess, 'run', return_value=subprocess.CompletedProcess([], status, '', 'no such pattern')):
                self.assertFalse(recon.extract_xss(str(source), str(self.output)))


class PipelineTests(unittest.TestCase):
    """Run the real script against local fixture executables, never real tools."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.script = self.root / 'bottest.py'
        self.script.write_text(Path(recon.__file__).read_text())
        bindir = self.root / 'bin'
        bindir.mkdir()
        fixture = '#!' + sys.executable + '\n' + r'''
import json
import os
from pathlib import Path
import sys
from urllib.parse import urlsplit
name = Path(sys.argv[0]).name
args = sys.argv[1:]
with open(os.environ['CALL_LOG'], 'a') as log:
    log.write(name + '\n')
if name == os.environ.get('FAIL_TOOL'):
    print('partial.example.com')
    sys.exit(3)
if name == 'subfinder':
    domain = args[args.index('-d') + 1]
    Path(args[args.index('-o') + 1]).write_text('' if os.environ.get('EMPTY_SUBS') else 'www.' + domain + '\n')
elif name == 'gau':
    print('https://' + args[-1] + '/archive')
elif name in ('dnsx', 'naabu'):
    for line in sys.stdin:
        print(line.strip() + (':443' if name == 'naabu' else ''))
elif name == 'httpx':
    if '-json' in args:
        for line in Path(args[args.index('-l') + 1]).read_text().splitlines():
            print(json.dumps({'url': 'https://' + line, 'status_code': 200}))
    else:
        for line in sys.stdin:
            print('https://' + line.strip())
elif name == 'katana':
    urls = [line.strip() + '/index.php?a=1' for line in sys.stdin]
    Path(args[args.index('-o') + 1]).write_text('\n'.join(urls) + '\n')
elif name == 'unfurl':
    for line in sys.stdin:
        print(urlsplit(line.strip()).hostname)
elif name == 'anew':
    path = Path(args[-1])
    lines = list(dict.fromkeys((path.read_text().splitlines() if path.exists() else []) + sys.stdin.read().splitlines()))
    path.write_text(''.join(line + '\n' for line in lines))
elif name == 'nuclei':
    sys.stdin.read()
    Path(args[args.index('-o') + 1]).write_text('')
elif name == 'gf':
    sys.stdin.read()
    sys.exit(1)
elif name == 'resolvhtml':
    Path(args[0]).write_text('<html>' + sys.stdin.read() + '</html>')
else:
    sys.exit('unexpected fixture tool: ' + name)
'''
        for tool in ['subfinder', 'gau', 'dnsx', 'naabu', 'httpx', 'katana', 'unfurl', 'anew', 'nuclei', 'gf']:
            executable = bindir / tool
            executable.write_text(fixture)
            executable.chmod(0o755)
        report = self.root / 'resolvhtml'
        report.write_text(fixture)
        report.chmod(0o755)
        self.calls = self.root / 'calls.txt'
        self.env = {**os.environ, 'PATH': str(bindir) + ':/usr/bin:/bin', 'CALL_LOG': str(self.calls)}

    def invoke(self, domain='example.com', **env):
        return subprocess.run([sys.executable, str(self.script)], input=domain + '\n',
                              cwd=self.root, env={**self.env, **env}, capture_output=True, text=True)

    def test_domain_isolation_and_successful_empty_scan_resumes(self):
        for domain in ['example.com', 'example.org']:
            result = self.invoke(domain)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            output = self.root / ('recon_' + domain)
            self.assertIn(domain, (output / (domain + '_http200.txt')).read_text())
            self.assertTrue((output / (domain + '_nuclei.txt.done.json')).exists())
        before = self.calls.read_text().splitlines()
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        after = self.calls.read_text().splitlines()
        self.assertEqual(after.count('subfinder'), before.count('subfinder'))
        self.assertEqual(after.count('nuclei'), before.count('nuclei'))
        self.assertEqual(after.count('httpx'), before.count('httpx'))

    def test_pipeline_failure_stops_then_retry_replaces_partial_output(self):
        result = self.invoke(FAIL_TOOL='dnsx')
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn('naabu', self.calls.read_text().splitlines())
        self.assertNotIn('Recon Summary', result.stdout)
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        live = self.root / 'recon_example.com/example.com_subs_live.txt'
        self.assertEqual(live.read_text(), 'www.example.com\n')

    def test_empty_upstream_removes_stale_downstream_and_report(self):
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        output = self.root / 'recon_example.com'
        (output / 'example.com_subs.txt.done.json').unlink()
        result = self.invoke(EMPTY_SUBS='1')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for name in ['http200.txt', 'http200.json', 'crawling.txt', 'fulldomains200.txt', 'nuclei.txt', 'dalfox.txt']:
            self.assertEqual((output / ('example.com_' + name)).read_text(), '')
        self.assertFalse((output / 'example.com_report.html').exists())


if __name__ == '__main__':
    unittest.main()
