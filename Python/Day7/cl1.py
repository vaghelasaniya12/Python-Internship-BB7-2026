
def make_greeting(language):

    def greeting(name):

        if language == "hindi":
            print("Namaste,", name)

        elif language == "english":
            print("Hello,", name)

        else:
            print("Language not supported")

    return greeting


hindi_greeting = make_greeting("hindi")
english_greeting = make_greeting("english")

hindi_greeting("Saniya")
english_greeting("Saniya")
