import sys
import lexer
import runtime
import os

def main():
    if len(sys.argv) < 2:
        print("Using: jppi main.jpp")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        sys.exit(1)

    if not file_path.endswith(".jpp"):
        print(f"Error: file {file_path} not extension jpp")
        sys.exit(1)

    instruction = lexer.load_jpp_file(file_path)
    runtime.run_instructions(instruction)

if __name__ == "__main__":
    main()
