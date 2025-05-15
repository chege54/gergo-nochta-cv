
import markdown
from pathlib import Path
import shutil
import os

CUSTOM_CSS = '<link rel="stylesheet" href="css/style.css">'

def convert_markdown_to_html(md: str, output_folder_path: Path):
    # Copy CSS
    css_template = Path(os.path.dirname(__file__)).joinpath("css")
    shutil.copytree(css_template, output_folder_path.joinpath("css"))

    # Generate HTML
    html_body = markdown.markdown(md, extensions=['fenced_code', 'extra'], output_format='html')
    output_path = output_folder_path.joinpath("index.html")

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>CV</title>
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

