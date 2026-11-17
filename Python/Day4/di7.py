
inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15,
    "Monitor": 5
}

# Adding new stock
inventory["Laptop"] += 5

print("After adding stock:", inventory)

# Selling an existing product
product = "Mouse"
quantity = 3

if product in inventory:
    if inventory[product] >= quantity:
        inventory[product] -= quantity
        print("Product sold successfully")
    else:
        print("Not enough stock")
else:
    print("Product not found")

# Selling a product that does not exist
product = "Mobile"

if product in inventory:
    inventory[product] -= 1
else:
    print("Product not found:", product)

print("Final Inventory:", inventory)
