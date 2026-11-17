numbers = [10, 20, 30, 40, 50, 50, 40, 20, 10, 30, 70, 70, 70]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("Original List:", numbers)
print("List Without Duplicates:", unique_numbers)