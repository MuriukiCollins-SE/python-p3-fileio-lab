from pathlib import Path

def write_file(file_name, file_content):
    # Ensure file_name is a Path object
    file_path = Path(f"{file_name}.txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_path = Path(f"{file_name}.txt")
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'a') as f:
        f.write(append_content)

def read_file(file_name):
    file_path = Path(f"{file_name}.txt")
    if not file_path.exists():
        return None
    with open(file_path, 'r') as f:
        return f.read()
