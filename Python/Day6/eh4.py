def read_file_safely(filename):
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()

        return content

    except FileNotFoundError:
        return "File not found"
print(read_file_safely("data.txt"))