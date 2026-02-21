

fileName1 = 'sample.txt'

try:
    with open(fileName1, 'r') as file:
        print("Reading file content:")


        lines = file.readlines()
        _serial = 1

        for line in lines:
            serial = _serial + 1
            print(f"Line {_serial}: {line.rstrip()}")



        # print(f"Line 1:", line1.replace("\n", ""))
        # print(f"Line 2:", line2.replace("\n", ""))


except FileNotFoundError:
    print(f"Error: The file '{fileName1}' was not found.")