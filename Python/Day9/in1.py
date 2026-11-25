class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
class Student(Person):
    def __init__(self, age, name, course):
        super().__init__(name, age)
        self.course = course
    
    def study(self):
        print(self.name, "is studying", self.course)
        
student1 = Student("Saniya", 21, "Python")

student1.display()
print("Course:", student1.course)
student1.study()


     
        