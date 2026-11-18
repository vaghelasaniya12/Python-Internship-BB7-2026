def calculate_sum(n):

    if n == 0:
        return 0

    else:
        return n + calculate_sum(n - 1)


result = calculate_sum(5)

print("Sum:", result)