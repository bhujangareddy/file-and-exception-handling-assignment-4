# Write and Append Data to a File

user_inp = input("Enter text to write to the file: ")

try: 
    with open("output.txt", "wt") as fh:
        data = fh.write(user_inp)
except Exception:
    print(Exception)
else:    
    print("Data Successfully written to output.txt.\n")

user_inp2 = input("Enter additional text to append: ")

try:
    with open("output.txt", "at") as fh:
        data = fh.write(f"\n{user_inp2}")
except Exception:
    print(Exception)
else:
    print("Data successfully appended.")
    print()
    print(f"Final content of output.txt:")

try:
    with open("output.txt", "rt") as fh:
        data = fh.read()
except Exception:
    print(Exception)
else:
    print(data)