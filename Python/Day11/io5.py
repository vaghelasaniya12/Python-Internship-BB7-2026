with open("my_story.txt", "r") as file:
    content = file.read()

    words = content.split()

    total_words = len(words)

    print("Total words:", total_words)