import time

def timer(func):

    def wrapper():

        start = time.time()

        func()

        end = time.time()

        print("Execution Time:", end - start, "seconds")

    return wrapper


@timer
def calculate_sum():

    total = sum(range(1, 1000001))

    print("Sum:", total)


calculate_sum()