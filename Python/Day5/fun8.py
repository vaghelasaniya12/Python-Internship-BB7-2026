def require_positive(func):

    def wrapper(*args, **kwargs):

        for value in args:
            if not isinstance(value, (int, float)) or value <= 0:
                print("Error: All arguments must be positive numbers!")
                return

        for value in kwargs.values():
            if not isinstance(value, (int, float)) or value <= 0:
                print("Error: All arguments must be positive numbers!")
                return

        return func(*args, **kwargs)

    return wrapper


@require_positive
def divide(a, b):

    print("Result:", a / b)


divide(20, 5)

divide(20, -5)

divide(20, 0)