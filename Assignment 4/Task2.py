# Define the filename
filename = "output.txt"

# 1. Take user input and write it to the file (Overwrites if file exists)
initial_text = input("Enter text to write to the file: ")
with open(filename, "w") as file:
    # Adding a newline character '\n' so the next entry starts on a new line
    file.write(initial_text + "\n")
print(f"Data successfully written to {filename}.\n")

# 2. Append additional data to the same file
additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.\n")

# 3. Read and display the final content of the file
print(f"Final content of {filename}:")
with open(filename, "r") as file:
    # .read() reads the whole file. .strip() removes the final blank line at the end.
    final_content = file.read().strip()
    print(final_content)