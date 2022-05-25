friends =["Ram", "Shyam", "Hari", "Sita"]

for friend in friends:
    print(f"{friend} is my friend.")

#Output
#Ram is my friend.
#Shyam is my friend.
#Hari is my friend.
#Sita is my friend.

#Example 2: get grades of a class
grades= [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades: # or we can just do sum(grades) instead of for loop
    total = total + grade # OR total += grade

#for average in class
print(total/amount)