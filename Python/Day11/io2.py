with open("my_story.txt", "r") as file:

    for line in file:
        print(line.strip(), "Length:", len(line.strip()))