import sys

def char_to_bae(c):
    return "bae" * ord(c)

def bae_to_char(b):
    return chr(len(b) // 3)

def py_to_bae(py_code):
    return "|".join(char_to_bae(c) for c in py_code)

def bae_to_py(bae_code):
    return "".join(bae_to_char(b) for b in bae_code.split("|"))

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def convert_to_bae(py_code):
    return py_to_bae(py_code)

def convert_to_py(bae_code):
    return bae_to_py(bae_code)

def main():
    if len(sys.argv) < 2:
        print("Usage: convert.py [file.bae|file.py]")
        sys.exit(1)

    file_path = sys.argv[1]

    if file_path.endswith(".bae"):
        bae_code = read_file(file_path)
        py_code = bae_to_py(bae_code)
        new_file_path = file_path.replace(".bae", ".py")
        write_file(new_file_path, py_code)
        print(f"Converted {file_path} to {new_file_path}")

    elif file_path.endswith(".py"):
        py_code = read_file(file_path)
        bae_code = py_to_bae(py_code)
        new_file_path = file_path.replace(".py", ".bae")
        write_file(new_file_path, bae_code)
        print(f"Converted {file_path} to {new_file_path}")

    else:
        print("Error: File must end with .bae or .py")
        sys.exit(1)

if __name__ == "__main__":
    main()
