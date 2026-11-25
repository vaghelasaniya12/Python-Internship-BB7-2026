
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if len(self.__items) == 0:
            return "Stack is empty"
        return self.__items.pop()

    def __str__(self):
        return str(self.__items)


# Creating object
s1 = Stack()

s1.push(10)
s1.push(20)
s1.push(30)

print("Stack:", s1)

print("Removed item:", s1.pop())

print("Updated Stack:", s1)
