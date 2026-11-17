students = [("Bheem", 88), ("Chutki", 95), ("Raju", 72), ("Jaggu", 78)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Students sorted by marks (highest to lowest):")
print(sorted_students)
