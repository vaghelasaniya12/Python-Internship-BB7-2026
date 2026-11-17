product = {
    "Laptop": 50000,
    "Mouse": 80,
    "Keyboard": 500,
    "Monitor": 8000,
    "Pen": 20,
    "Headphones": 1500,
}

expensive_products = {name: price for name, price in product.items() if price > 100}

print("All products:", product)
print("Products above 100:", expensive_products)
