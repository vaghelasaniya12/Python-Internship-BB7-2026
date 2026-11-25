
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


# Creating objects
p1 = Point(10, 20)
p2 = Point(10, 20)
p3 = Point(5, 15)

print(p1)
print(p2)

print(p1 == p2)
print(p1 == p3)
