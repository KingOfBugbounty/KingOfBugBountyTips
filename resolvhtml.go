package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"html/template"
	"os"
	"strings"
)

// Define a struct to match the JSON structure
type HTTPXData struct {
	Timestamp     string `json:"timestamp"`
	Port          string `json:"port"`
	URL           string `json:"url"`
	Input         string `json:"input"`
	Location      string `json:"location"`
	Title         string `json:"title"`
	Scheme        string `json:"scheme"`
	ContentType   string `json:"content_type"`
	Method        string `json:"method"`
	Host          string `json:"host"`
	Path          string `json:"path"`
	Time          string `json:"time"`
	A             []string `json:"a"`
	Words         int    `json:"words"`
	Lines         int    `json:"lines"`
	StatusCode    int    `json:"status_code"`
	ContentLength int    `json:"content_length"`
	Failed        bool   `json:"failed"`
	KnowledgeBase struct {
		PageType string `json:"PageType"`
		PHash    int    `json:"pHash"`
	} `json:"knowledgebase"`
}

// Function to convert JSON data from stdin to HTML
func convertJSONToHTML(outputFile string) error {
	// Create or open the HTML output file
	htmlFile, err := os.Create(outputFile)
	if err != nil {
		return fmt.Errorf("failed to create output file: %v", err)
	}
	defer htmlFile.Close()

	// Define the HTML template with Dracula theme
	const tmpl = `
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>HTTPX Data Report</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            background-color: #282a36; 
            color: #f8f8f2; 
            margin: 0; 
            padding: 20px; 
        }
        table { 
            width: 100%; 
            border-collapse: collapse; 
            margin-top: 20px; 
        }
        th, td { 
            border: 1px solid #44475a; 
            padding: 8px; 
            text-align: left; 
        }
        th { 
            background-color: #50fa7b; 
            color: #282a36; 
        }
        tr:nth-child(even) { 
            background-color: #44475a; 
        }
        tr:nth-child(odd) { 
            background-color: #282a36; 
        }
        input[type="text"] { 
            padding: 10px; 
            margin: 10px 0; 
            border: 1px solid #6272a4; 
            border-radius: 4px; 
            background-color: #44475a; 
            color: #f8f8f2; 
        }
        input[type="text"]::placeholder { 
            color: #6272a4; 
        }
    </style>
</head>
<body>
    <h1>HTTPX Data Report</h1>
    <input type="text" id="searchInput" placeholder="Search...">
    <table>
        <thead>
            <tr>
                <th>Timestamp</th>
                <th>Port</th>
                <th>URL</th>
                <th>Input</th>
                <th>Location</th>
                <th>Title</th>
                <th>Scheme</th>
                <th>Content Type</th>
                <th>Method</th>
                <th>Host</th>
                <th>Path</th>
                <th>Time</th>
                <th>A</th>
                <th>Words</th>
                <th>Lines</th>
                <th>Status Code</th>
                <th>Content Length</th>
                <th>Failed</th>
                <th>KnowledgeBase PageType</th>
                <th>KnowledgeBase pHash</th>
            </tr>
        </thead>
        <tbody>
            {{range .}}
            <tr>
                <td>{{.Timestamp}}</td>
                <td>{{.Port}}</td>
                <td>{{.URL}}</td>
                <td>{{.Input}}</td>
                <td>{{.Location}}</td>
                <td>{{.Title}}</td>
                <td>{{.Scheme}}</td>
                <td>{{.ContentType}}</td>
                <td>{{.Method}}</td>
                <td>{{.Host}}</td>
                <td>{{.Path}}</td>
                <td>{{.Time}}</td>
                <td>{{join .A ", "}}</td>
                <td>{{.Words}}</td>
                <td>{{.Lines}}</td>
                <td>{{.StatusCode}}</td>
                <td>{{.ContentLength}}</td>
                <td>{{.Failed}}</td>
                <td>{{.KnowledgeBase.PageType}}</td>
                <td>{{.KnowledgeBase.PHash}}</td>
            </tr>
            {{end}}
        </tbody>
    </table>
    <script>
        document.getElementById('searchInput').addEventListener('keyup', function() {
            var input = this.value.toLowerCase();
            var rows = document.querySelectorAll('tbody tr');
            rows.forEach(function(row) {
                var cells = row.querySelectorAll('td');
                var match = Array.from(cells).some(function(cell) {
                    return cell.textContent.toLowerCase().includes(input);
                });
                row.style.display = match ? '' : 'none';
            });
        });
    </script>
</body>
</html>
`

	// Define the template function to join slice elements
	funcMap := template.FuncMap{
		"join": strings.Join,
	}

	t, err := template.New("report").Funcs(funcMap).Parse(tmpl)
	if err != nil {
		return fmt.Errorf("failed to parse template: %v", err)
	}

	// Read JSON data from stdin
	var httpxData []HTTPXData
	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		line := scanner.Text()
		var record HTTPXData
		if err := json.Unmarshal([]byte(line), &record); err != nil {
			fmt.Fprintf(os.Stderr, "Failed to parse JSON line: %v\n", err)
			continue
		}
		httpxData = append(httpxData, record)
	}

	if err := scanner.Err(); err != nil {
		return fmt.Errorf("error reading from stdin: %v", err)
	}

	// Write HTML report
	return t.Execute(htmlFile, httpxData)
}

func main() {
	if len(os.Args) != 2 {
		fmt.Fprintf(os.Stderr, "Usage: %s <output HTML file>\n", os.Args[0])
		os.Exit(1)
	}
	outputFile := os.Args[1]

	err := convertJSONToHTML(outputFile)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error converting JSON to HTML: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Successfully converted JSON to HTML and saved to %s\n", outputFile)
}

