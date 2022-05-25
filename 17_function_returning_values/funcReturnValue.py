# Example1
# value returning functions
def add(x, y):
    return x + y

print(add(5,6))
#Output: 11

# Example2
# math argument
def divide(dividend, divisor):
    if divisor!= 0:
        return dividend/divisor
    else:
        return "Hello World!"

result = divide(dividend=15,divisor=3) 
print(result)