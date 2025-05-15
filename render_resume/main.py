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

    parser.add_argument(
        '--image',
        required=True,
        help="Path to an existing image file (.png, .jpg, .jpeg, .bmp, .tiff, .gif)"
    )

    args = parser.parse_args()
    output_folder = get_output_folder()

    # Encode image for embedding
    # profile_image_b64 = encode_image_to_base64(args.image)
    input_image_path = Path(args.image)
    if input_image_path.exists() and input_image_path.suffix in [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".webp"]:
        profile_image_name = "profile" + input_image_path.suffix
        profile_image_path = Path(shutil.copyfile(
            input_image_path, output_folder.joinpath(profile_image_name)))
    else:
        print(f"Given {input_image_path} not found of not supported format!")
        profile_image_name = ""

    # Collect data from exported CSVs
    resume_data = collect_resume_data(args.folder)

    # Jinja2 markdown rendering
    md = render_to_markdown(
        resume_data=resume_data, profile_image=profile_image_name, output_folder_path=output_folder)

    # HTML rendering
    convert_markdown_to_html(md=md, output_folder_path=output_folder)
