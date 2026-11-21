
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
            print("Salary increased successfully!")
        else:
            raise ValueError("Salary cannot be decreased or remain the same!")


emp1 = Employee(30000)

print("Original salary:", emp1.get_salary())

emp1.set_salary(40000)
print("Updated salary:", emp1.get_salary())

try:
    emp1.set_salary(25000)
except ValueError as e:
    print("Error:", e)
