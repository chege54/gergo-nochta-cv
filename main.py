import csv
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

INPUT_FILES = [   
    'Education.csv',
    'Email Addresses.csv',
    'Honors.csv',
    'Languages.csv',
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
            sanitized_keys.append({k.replace(' ', ''): v for k, v in r.items()})
        file_stem = str(file_path.stem).replace(' ', '')
        self.data.update({ f"{file_stem}" : sanitized_keys })
                   
    
if __name__ == "__main__":
    
    # Collect data from exported CSVs
    resume = Resume()
    for file_name in INPUT_FILES:
        file_path =  Path(f"cv/Basic_LinkedInDataExport_05-12-2025/{file_name}")
        resume.update_resume_data(file_path)
    
    # Jinja2 rendering
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('markdown.jinja')

    output = template.render(resume=resume.data)

    with open('resume.md', 'w') as f:
        f.write(output)
