numbers = [10, 50, 30, 60, 70, 20, 90, 40, 80]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num
print ("Largest number:", largest)
print ("Second largest number:", second_largest)