filename = "output.txt"

initial_text = input("Enter text to write to the file: ")
#open file to write in write mode.
with open(filename, "w") as file:
    file.write(initial_text + "\n")
print(f"Data successfully written to {filename}.\n")

#Add additional text using 'a' append mode
additional_text = input("Enter additional text to append: ")
with open(filename, "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.\n")
print(f"Final content of {filename}:")
with open(filename, "r") as file:
    final_content = file.read().strip()
    print(final_content)