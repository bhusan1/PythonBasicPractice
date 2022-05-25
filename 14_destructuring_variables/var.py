t = 5, 11 # t is tupple : so, when x, y is = t, x and y get values 5 , 11
x, y = t

print(x , y)    # 5, 11


#also we can assign values like this:
x, y = 12, 22
print(x, y)      #12, 22

# destructuring variables 
people =[("Ben", 40, "Teacher"),("Beau", 5, "Dog"),("Betty", 22, "Student")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

#Output:
#Name: Ben, Age: 40, Profession: Teacher
#Name: Beau, Age: 5, Profession: Dog
#Name: Betty, Age: 22, Profession: Student