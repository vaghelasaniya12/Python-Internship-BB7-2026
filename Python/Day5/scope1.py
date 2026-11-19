count = 0 
def counter():
    global count
    count += 1
    
counter()
counter()
counter()
counter()

print("Function called", count, "times.")
