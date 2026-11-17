employees = {
    "Ayman": 10000,
    "Fatima": 20000,
    "Nihaa": 30000,
    "Sheesh": 40000,
    "Hayaa": 50000
}

sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)

print("Top 3 highest paid employees:")

for name, salary in sorted_employees[:3]:
    print(name, ":", salary)