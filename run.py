import sys

def bae_to_char(b):
    return chr(len(b) // 3)

def bae_to_py(bae_code):
    return "".join(bae_to_char(b) for b in bae_code.split("|"))

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_bae(bae_code):
    py_code = bae_to_py(bae_code)
    exec(py_code)

def main():
    if len(sys.argv) < 2:
        print("Usage: run.py [file.bae]")
        sys.exit(1)

    file_path = sys.argv[1]

    if not file_path.endswith(".bae"):
        print("Error: Only .bae files can be executed.")
        sys.exit(1)

    bae_code = read_file(file_path)
    execute_bae(bae_code)

if __name__ == "__main__":
    main()
