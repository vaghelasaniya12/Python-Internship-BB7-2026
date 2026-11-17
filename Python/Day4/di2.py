students = [
    {"name": "Saniya", "marks": 88},
    {"name": "Ayman", "marks": 95},
    {"name": "Sara", "marks": 72},
    {"name": "Khadijah", "marks": 91}
]

highest_student = students[0]

for student in students:
    if student["marks"] > highest_student["marks"]:
        highest_student = student
        
print("Topper:", highest_student["name"])
print("Highest Marks:", highest_student["marks"])
