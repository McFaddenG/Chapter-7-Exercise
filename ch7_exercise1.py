fn = input("Enter the file name: ")

try:
    with open(fn, 'r') as file:
        for line in file:
            print(line.upper(), end='')
except FileNotFoundError:
    print(f"Error: file '{fn}' not found.")
