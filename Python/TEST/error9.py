marks = [80, 75, 90, 65, 70]

total = 0

for mark in marks:
    total += mark

percentage = total / 500 * 100

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("Total:", total)
print("Percentage:", percentage)
print("Result:", result)

#Total: 380
#Percentage: 76.0
#Result: PASS