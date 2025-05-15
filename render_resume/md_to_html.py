
import markdown
from pathlib import Path

CUSTOM_CSS = """
<style>
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f9f9f9;
    margin: 40px;
    line-height: 1.6;
    color: #333;
}
h1, h2, h3 {
    color: #005a9c;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}
table, th, td {
    border: 1px solid #ccc;
}
th, td {
    padding: 8px;
    text-align: left;
}
code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 4px;
}
</style>
"""

def convert_markdown_to_html(md: str, output_folder_path: Path):
    html_body = markdown.markdown(md, extensions=['fenced_code', 'tables', 'extra', 'toc'], output_format='html')
    output_path = output_folder_path.joinpath("index.html")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Styled Markdown Output</title>
        {CUSTOM_CSS}
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """

    with open(output_path, mode="w") as f:
        f.write(html_content)
        print(f"HTML resume saved to {output_path}")

