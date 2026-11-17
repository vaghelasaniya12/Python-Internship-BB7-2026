tasks = []

tasks.append("Study Python")
tasks.append("Complete Internship")
tasks.append("Practice List")
tasks.append("Learn Functions")
tasks.append("Revise Loops")

print("Tasks after adding:")
for task in tasks:
    print(task)
    
tasks.remove("Practice List")
tasks.remove("Learn Functions")

print("\nTasks after removing:")
for task in tasks:
    print(task)