# Templates

Reusable scan templates and PoC fixtures referenced from the tips in
[`docs/`](../docs/). See [`../CONTRIBUTING.md`](../CONTRIBUTING.md) before
adding a new one.

## `nuclei/`

Nuclei templates (`nuclei -t templates/nuclei/<file>.yaml -u <target>`):

| Template | Detects |
|:---------|:--------|
| [`docker2.yaml`](nuclei/docker2.yaml) | Exposed/accessible Docker Registry API (`/v2/`, `/v2/_catalog`). |
| [`graphql-OFJAAAH.yaml`](nuclei/graphql-OFJAAAH.yaml) | Common GraphQL endpoint paths (`/graphql`, `/graphiql`, `/altair`, `/explorer`, …). |
| [`OFJAAAH-cpanelXSS.yaml`](nuclei/OFJAAAH-cpanelXSS.yaml) | A reflected XSS in cPanel. |

## `payloads/`

| File | Purpose |
|:-----|:--------|
| [`swagger.json`](payloads/swagger.json) / [`swagger.yaml`](payloads/swagger.yaml) | Swagger-UI XSS PoC pair — `swagger.json` points Swagger UI's "URL" field at the raw `swagger.yaml` in this repo, whose `info.description` carries an `onerror` XSS payload. Load `swagger.json`'s raw URL into a target's Swagger UI "Explore" box to test for unsanitized spec rendering. See [`docs/api-security.md`](../docs/api-security.md). |

See also [`../data/`](../data/) for plain payload/data lists (SSRF bypass
strings, sample URL lists) that aren't Nuclei templates.
