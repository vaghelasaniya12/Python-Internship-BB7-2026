from functools import reduce

numbers = [10, 45, 23, 89, 12, 67]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest Number:", largest)