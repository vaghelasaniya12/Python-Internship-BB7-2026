cart = [
    ["Keyboard", 800],
    ["Mouse", 400],
    ["USB Cable", 200]
]

total = 0

for item in cart:
    total += item[1]

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_amount = total - discount

print("Total:", total)
print("Discount:", discount)
print("Final Amount:", final_amount)

# Total: 1400
# Discount: 140.0
# Final Amount: 1260.0