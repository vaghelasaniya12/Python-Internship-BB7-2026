with open("input.txt", "r") as file:
    content = file.read()

with open("copy.txt", "w") as new_file:
    new_file.write(content)

print("File copied successfully!")