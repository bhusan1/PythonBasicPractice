# first class functions
# here divide class is used as a value for operator parameter
# # so both operator and divide represent divide method 

def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

def calculate(*values, operator):
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)
