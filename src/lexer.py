import os
import sys
# libs

def load_jpp_file(file_path):
    if not file_path.endswith('.jpp'):
        print("Critical error: Not found extension .jpp")
        sys.exit(1)

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found!")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    clean_lines = []
    for line in code.split('\n'):
        line = line.strip()
        if not line or line.startswith('//'):
            continue
        if '//' in line:
            line = line.split('//')[0].strip()


        clean_lines.append(line)

    return clean_lines
