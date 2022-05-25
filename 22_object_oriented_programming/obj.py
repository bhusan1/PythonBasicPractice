# creating class Student and defining 2 methods init and average
# # self is an object|| it can be named anything
class Student:
    def __init__(self):
        self.name = "Rolf"
        self.grades = (90, 91, 92, 93, 88, 85)
    
    def average(self):
        return sum(self.grades) / len(self.grades)

## here student variable is cretaed to pass as object inside Student 
student = Student()
print(student.name)
print(student.grades)
print(student.average()) ## also use it as Student.average(student)