## init method can also take arguments or parameters
class Student:
    def __init__(self, name, grade):
        self.name = name    ## passing the name and grade parameter from student variable
        self.grades = grade
    
    def average(self):
        return sum(self.grades) / len(self.grades)

## here student variable is cretaed to pass as object inside Student 
# passing parameter name and grade || self is passed default as student
student = Student("Bob", (90, 91, 92, 93, 88, 85))    
print(student.name)
print(student.average())

## Output
# Bob
# 89.83333333333333