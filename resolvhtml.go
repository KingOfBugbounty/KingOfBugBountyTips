package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"html/template"
	"os"
	"strings"
)

type HTTPXData struct {
	Timestamp     string   `json:"timestamp"`
	Port          string   `json:"port"`
	URL           string   `json:"url"`
	Input         string   `json:"input"`
	Location      string   `json:"location"`
	Title         string   `json:"title"`
	Scheme        string   `json:"scheme"`
	ContentType   string   `json:"content_type"`
	Method        string   `json:"method"`
	Host          string   `json:"host"`
	Path          string   `json:"path"`
	Time          string   `json:"time"`
	A             []string `json:"a"`
	Words         int      `json:"words"`
	Lines         int      `json:"lines"`
	StatusCode    int      `json:"status_code"`
	ContentLength int      `json:"content_length"`
	Failed        bool     `json:"failed"`
	KnowledgeBase struct {
		PageType string `json:"PageType"`
		PHash    int    `json:"pHash"`
	} `json:"knowledgebase"`
}

func statusClass(code int) string {
	switch {
	case code >= 500:
		return "s5xx"
	case code >= 400:
		return "s4xx"
	case code >= 300:
		return "s3xx"
	case code >= 200:
		return "s2xx"
	default:
		return ""
	}
}

func convertJSONToHTML(outputFile string) error {
	htmlFile, err := os.Create(outputFile)
	if err != nil {
		return fmt.Errorf("failed to create output file: %v", err)
	}
	defer htmlFile.Close()

	const tmpl = `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HTTPX Report</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Courier New', monospace;
            background: #282a36;
            color: #f8f8f2;
            padding: 20px;
        }
        h1 { color: #50fa7b; margin-bottom: 16px; font-size: 1.4rem; }

        /* Summary bar */
        .summary {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }
        .stat {
            background: #44475a;
            border-radius: 6px;
            padding: 10px 18px;
            text-align: center;
            min-width: 90px;
        }
        .stat .num { font-size: 1.6rem; font-weight: bold; }
        .stat .lbl { font-size: 0.7rem; color: #6272a4; margin-top: 2px; }
        .stat.total .num { color: #f8f8f2; }
        .stat.s2xx  .num { color: #50fa7b; }
        .stat.s3xx  .num { color: #f1fa8c; }
        .stat.s4xx  .num { color: #ffb86c; }
        .stat.s5xx  .num { color: #ff5555; }

        /* Search */
        input[type="text"] {
            padding: 8px 12px;
            margin-bottom: 14px;
            width: 320px;
            border: 1px solid #6272a4;
            border-radius: 4px;
            background: #44475a;
            color: #f8f8f2;
            font-family: inherit;
        }
        input[type="text"]::placeholder { color: #6272a4; }

        /* Table */
        table { width: 100%; border-collapse: collapse; font-size: 0.82rem; }
        th, td { border: 1px solid #44475a; padding: 6px 8px; text-align: left; }
        th {
            background: #44475a;
            color: #50fa7b;
            cursor: pointer;
            user-select: none;
            white-space: nowrap;
        }
        th:hover { background: #5a5d6e; }
        th.asc::after  { content: " ▲"; }
        th.desc::after { content: " ▼"; }
        tr:nth-child(even) { background: #313342; }
        tr:nth-child(odd)  { background: #282a36; }
        tr:hover { background: #3d4058; }

        /* Links */
        a { color: #8be9fd; text-decoration: none; }
        a:hover { text-decoration: underline; }

        /* Status code colors */
        .s2xx { color: #50fa7b; font-weight: bold; }
        .s3xx { color: #f1fa8c; font-weight: bold; }
        .s4xx { color: #ffb86c; font-weight: bold; }
        .s5xx { color: #ff5555; font-weight: bold; }
    </style>
</head>
<body>
    <h1>HTTPX Report</h1>

    <div class="summary">
        <div class="stat total"><div class="num" id="cnt-total">0</div><div class="lbl">Total</div></div>
        <div class="stat s2xx"> <div class="num" id="cnt-2xx">0</div><div class="lbl">2xx</div></div>
        <div class="stat s3xx"> <div class="num" id="cnt-3xx">0</div><div class="lbl">3xx</div></div>
        <div class="stat s4xx"> <div class="num" id="cnt-4xx">0</div><div class="lbl">4xx</div></div>
        <div class="stat s5xx"> <div class="num" id="cnt-5xx">0</div><div class="lbl">5xx</div></div>
    </div>

    <input type="text" id="search" placeholder="Search…" oninput="filterRows()">

    <table id="tbl">
        <thead>
            <tr>
                <th onclick="sortTable(0)">Timestamp</th>
                <th onclick="sortTable(1)">Port</th>
                <th onclick="sortTable(2)">URL</th>
                <th onclick="sortTable(3)">Title</th>
                <th onclick="sortTable(4)">Status</th>
                <th onclick="sortTable(5)">Content-Type</th>
                <th onclick="sortTable(6)">Length</th>
                <th onclick="sortTable(7)">Words</th>
                <th onclick="sortTable(8)">Lines</th>
                <th onclick="sortTable(9)">Host</th>
                <th onclick="sortTable(10)">IPs</th>
                <th onclick="sortTable(11)">Failed</th>
            </tr>
        </thead>
        <tbody>
            {{range .}}
            <tr>
                <td>{{.Timestamp}}</td>
                <td>{{.Port}}</td>
                <td><a href="{{.URL}}" target="_blank" rel="noopener">{{.URL}}</a></td>
                <td>{{.Title}}</td>
                <td class="{{statusClass .StatusCode}}">{{.StatusCode}}</td>
                <td>{{.ContentType}}</td>
                <td>{{.ContentLength}}</td>
                <td>{{.Words}}</td>
                <td>{{.Lines}}</td>
                <td>{{.Host}}</td>
                <td>{{join .A ", "}}</td>
                <td>{{.Failed}}</td>
            </tr>
            {{end}}
        </tbody>
    </table>

    <script>
        // ── Summary counts ──────────────────────────────────────────────────
        (function () {
            var rows = document.querySelectorAll('#tbl tbody tr');
            var t = 0, s2 = 0, s3 = 0, s4 = 0, s5 = 0;
            rows.forEach(function (r) {
                var sc = parseInt(r.cells[4].textContent, 10);
                t++;
                if      (sc >= 500) s5++;
                else if (sc >= 400) s4++;
                else if (sc >= 300) s3++;
                else if (sc >= 200) s2++;
            });
            document.getElementById('cnt-total').textContent = t;
            document.getElementById('cnt-2xx').textContent   = s2;
            document.getElementById('cnt-3xx').textContent   = s3;
            document.getElementById('cnt-4xx').textContent   = s4;
            document.getElementById('cnt-5xx').textContent   = s5;
        })();

        // ── Search / filter ─────────────────────────────────────────────────
        function filterRows() {
            var q = document.getElementById('search').value.toLowerCase();
            document.querySelectorAll('#tbl tbody tr').forEach(function (r) {
                r.style.display = r.textContent.toLowerCase().includes(q) ? '' : 'none';
            });
        }

        // ── Column sort ─────────────────────────────────────────────────────
        var sortState = { col: -1, dir: 1 };

        function sortTable(col) {
            var tbody = document.querySelector('#tbl tbody');
            var rows  = Array.from(tbody.querySelectorAll('tr'));
            var ths   = document.querySelectorAll('#tbl thead th');

            ths.forEach(function (th) { th.classList.remove('asc', 'desc'); });

            if (sortState.col === col) {
                sortState.dir *= -1;
            } else {
                sortState.col = col;
                sortState.dir = 1;
            }
            ths[col].classList.add(sortState.dir === 1 ? 'asc' : 'desc');

            rows.sort(function (a, b) {
                var av = a.cells[col].textContent.trim();
                var bv = b.cells[col].textContent.trim();
                var an = parseFloat(av), bn = parseFloat(bv);
                if (!isNaN(an) && !isNaN(bn)) return sortState.dir * (an - bn);
                return sortState.dir * av.localeCompare(bv);
            });
            rows.forEach(function (r) { tbody.appendChild(r); });
        }
    </script>
</body>
</html>`

	funcMap := template.FuncMap{
		"join":        strings.Join,
		"statusClass": statusClass,
	}

	t, err := template.New("report").Funcs(funcMap).Parse(tmpl)
	if err != nil {
		return fmt.Errorf("failed to parse template: %v", err)
	}

	var data []HTTPXData
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		var record HTTPXData
		if err := json.Unmarshal([]byte(line), &record); err != nil {
			fmt.Fprintf(os.Stderr, "Skipping invalid JSON line: %v\n", err)
			continue
		}
		data = append(data, record)
	}
	if err := scanner.Err(); err != nil {
		return fmt.Errorf("error reading stdin: %v", err)
	}

	return t.Execute(htmlFile, data)
}

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <output.html>\n", os.Args[0])
		os.Exit(1)
	}
	if err := convertJSONToHTML(os.Args[1]); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
	fmt.Printf("Report saved to %s\n", os.Args[1])
}
