filename = 'sample.txt'

try:
    # Attempt to open the file in read mode
    with open(filename, 'r') as file:
        print("Reading file content:")

        # Iterate through each line in the file
        # enumerate(..., start=1) gives us a line counter starting at 1
        for line_number, line in enumerate(file, start=1):
            # .strip() removes the invisible newline characters at the end of each line
            print(f"Line {line_number}: {line.strip()}")

except FileNotFoundError:
    # This block catches the specific error when the file does not exist
    print(f"Error: The file '{filename}' was not found.")