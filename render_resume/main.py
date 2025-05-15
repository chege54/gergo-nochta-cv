import argparse
from base64_encode import encode_image_to_base64
from resume import collect_resume_data
from render_markdown import render_to_markdown
from md_to_html import convert_markdown_to_html
import os
from pathlib import Path
import shutil


def get_output_folder() -> Path:
    folder = Path(os.getcwd()).joinpath("output")
    if folder.exists():
        shutil.rmtree(folder)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Process folder and an image file.")
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

    args = parser.parse_args()
    output_folder = get_output_folder()

    # Encode image for embedding
    profile_image_b64 = encode_image_to_base64(args.image)

    # Collect data from exported CSVs
    resume_data = collect_resume_data(args.folder)

    # Jinja2 markdown rendering
    md = render_to_markdown(
        resume_data=resume_data, profile_image_b64=profile_image_b64, output_folder_path=output_folder)

    # HTML rendering
    convert_markdown_to_html(md=md, output_folder_path=output_folder)
