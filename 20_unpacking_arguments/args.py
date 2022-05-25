# '*' this symbol is used to unpack any number of arguments or elements from a list
# multiple arguments in a single variable when calling a function
# args does dictionary unpacking with positional arguments
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total
print(multiply(1, 3, 5))

'''
positional arguments -- 
'''



# example 2
def add (x, y):
    return x + y

nums = [3, 5]
add(*nums)  # this will add each element of nums as x and y


# example3
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return("No valid operator provided to apply( ).")

print(apply(1, 3, 5, 8, operator="+"))
#Output = 17
print(apply(1, 3, 5, 8, operator="*"))