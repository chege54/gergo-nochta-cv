
import markdown
from pathlib import Path

def convert_markdown_to_html(md: str, output_folder_path: Path):
    html = markdown.markdown(md, extensions=['fenced_code', 'codehilite', 'tables'])
    output_path = output_folder_path.joinpath("index.html")

    with open(output_path, mode="w") as f:
        f.write(html)
        print(f"HTML resume saved to {output_path}")
