# Read a File and Handle Errors

file_name = "sample.txt"

try:
    with open(file_name, "rt") as fh:
        data = fh.read() 
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
else:
    print(data)