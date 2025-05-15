from jinja2 import Environment, FileSystemLoader
import argparse
from base64_encode import encode_image_to_base64
from resume import collect_resume_data
import os
from pathlib import Path
import shutil

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_output_folder() -> Path:
    output_folder = Path(os.path.join(MODULE_DIR, "../output"))
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    return output_folder


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Process folder and an image file.")
    parser.add_argument(
        '--folder',
        required=True,
        help="Path of the export"
    )
    # TODO: check file is valid
    parser.add_argument(
        '--image',
        required=True,
        help="Path to an existing image file (.png, .jpg, .jpeg, .bmp, .tiff, .gif)"
    )
    parser.add_argument(
        '--output',
        default='resume.md',
        help="Output file name",
        required=False,
    )
    args = parser.parse_args()

    # Encode image for embedding
    profile_image_b64 = encode_image_to_base64(args.image)

    # Collect data from exported CSVs
    resume_data = collect_resume_data(args.folder)

    # Jinja2 rendering
    env = Environment(loader=FileSystemLoader(f"{MODULE_DIR}/../templates/"),  trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("markdown.jinja") # TODO: add multiple templates

    output_path = get_output_folder().joinpath(args.output)
    with open(output_path, mode="w") as f:
        rendered_output = template.render(resume=resume_data, profile_image_b64=profile_image_b64)
        f.write(rendered_output)
        print(f"Markdown resume saved to {output_path}")
