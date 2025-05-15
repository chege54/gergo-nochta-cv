from pathlib import Path
import csv
import os

INPUT_FILES = [
    'Education.csv',
    'Email Addresses.csv',
    # 'Honors.csv',
    'Languages.csv',
    'PhoneNumbers.csv',
    'Positions.csv',
    'Profile Summary.csv',
    'Profile.csv',
    'Skills.csv',
]


def read_csv(file_path):
    with open(file=file_path, mode='r') as f:
        csv_reader = csv.DictReader(f)
        parsed = [row for row in csv_reader]
        return parsed


class Resume:
    def __init__(self):
        self.data = {}

    def update_resume_data(self, file_path:Path):
        raw = read_csv(file_path)
        sanitized_keys = []
        for r in raw:
            sanitized = {k.replace(' ', ''): v.strip() for k, v in r.items() if v}
            if sanitized:
                sanitized_keys.append(sanitized)

        file_stem = str(file_path.stem).replace(' ', '')
        self.data.update({ f"{file_stem}" : sanitized_keys })


def collect_resume_data(folder:str) -> dict:
    resume = Resume()
    for file_name in INPUT_FILES:
        file_path =  Path(os.path.join(folder, file_name))
        if file_path.exists():
            resume.update_resume_data(file_path)
        else:
            print(f"File: '{file_path}' not found.")

    return resume.data
