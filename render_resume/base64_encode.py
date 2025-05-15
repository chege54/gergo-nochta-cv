import base64
from pathlib import Path


def encode_image_to_base64(path: str) -> str:
    image_path =  Path(path)
    img_b64 = b""
    if image_path.exists():
        with open(path, mode='rb') as img:
            img_b64 = base64.b64encode(img.read())
    else:
        print(f"File: '{image_path}' not found.")

    return img_b64.decode('ascii')


if __name__ == "__main__":
    TEST_PATH = "../profile1.jpg"
    encoded_str = encode_image_to_base64(path=TEST_PATH)
    print(encoded_str)
