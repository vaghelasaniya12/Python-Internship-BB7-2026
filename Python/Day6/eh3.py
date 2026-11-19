class InvalidAgeError(Exception):
    pass


def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError("Invalid age! Age must be between 0 and 120.")

    else:
        return "User registered successfully."


try:
    print(register_user(25))
    print(register_user(150))

except InvalidAgeError as e:
    print(e)