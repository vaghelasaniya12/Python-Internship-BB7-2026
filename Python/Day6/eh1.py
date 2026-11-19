def safe_division(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except TypeError:
        return "Error: Please enter valid numbers."


print(safe_division(10, 2))
print(safe_division(10, 0))
print(safe_division(10, "abc"))