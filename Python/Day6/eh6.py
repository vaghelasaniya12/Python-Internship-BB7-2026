def process_order(order):
    try:
        item = order["item"]
        price = order["price"]

    except KeyError:
        print("Error: Required key is missing.")

    else:
        print("Order Details:")
        print("Item:", item)
        print("Price:", price)

    finally:
        print("Processing complete.")


order1 = {"item": "Laptop", "price": 50000}
order2 = {"item": "Mobile"}

process_order(order1)

print()

process_order(order2)