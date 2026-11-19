
def make_validator(min_value):

    def validator(number):

        if number >= min_value:
            return True
        else:
            return False

    return validator


validator1 = make_validator(18)
validator2 = make_validator(50)

print("Validator 1:")
print(validator1(20))
print(validator1(15))

print("Validator 2:")
print(validator2(60))
print(validator2(30))
