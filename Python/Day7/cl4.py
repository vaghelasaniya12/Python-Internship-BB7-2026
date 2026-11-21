
mode = "Global Mode"

def outer():

    mode = "Enclosing Mode"

    def inner():

        mode = "Local Mode"
        print("Inside inner function:", mode)

    inner()

    print("Inside outer function:", mode)


outer()

print("Outside functions:", mode)
