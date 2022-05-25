# lambda are functions without a name: we can assign them name 

# this is a regular function
def add(x,y):
    return x + y

print(add(5,6))
#Output: 11

# this written as lambda function
print((lambda x, y: x + y)(5, 6))


# Example 2
def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
#doubled = map(double, sequence) -- also can use map fuction
print(doubled)

# this whole function as lambda function
sequence1 = [1, 3, 5, 9]
doubled1 = list(map(lambda x: x * 2, sequence )) # list is used because map return map object so must turn it to list
print(doubled1)
