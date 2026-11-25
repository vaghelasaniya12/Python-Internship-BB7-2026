class Employee:
    def calculate_salary(self):
        return 30000

class Developer(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = 10000
        return base_salary + bonus
    
class Designer(Employee):
    def calculate_salary(self):
        base_salary = super().calculate_salary()
        bonus = 5000
        return base_salary + bonus
    
dev = Developer()
des = Designer()

print("Developr's Salary:", dev.calculate_salary())
print("Designer's Salary:", des.calculate_salary())