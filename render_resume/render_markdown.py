from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import os


def render_to_markdown(resume_data: dict, profile_image_b64: str, output_folder_path: Path) -> str:

    template_folder = Path(os.path.dirname(__file__)).joinpath("templates")
    env = Environment(loader=FileSystemLoader(template_folder),
                      trim_blocks=True, lstrip_blocks=True)
    # TODO: add multiple templates
    template = env.get_template("markdown.jinja")

    rendered_output = template.render(
        resume=resume_data, profile_image_b64=profile_image_b64)

    output_path = output_folder_path.joinpath("cv.md")
    with open(output_path, mode="w") as f:
        f.write(rendered_output)
        print(f"Markdown resume saved to {output_path}")

    return rendered_output
