
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


# Creating object
inv = Inventory()

inv.add_item("Laptop")
inv.add_item("Mobile")
inv.add_item("Keyboard")

print("Total items:", len(inv))
print("First item:", inv[0])
print("Second item:", inv[1])
