# parameter
def add(x, y):
    result = x + y
    print(result)

# argument -- each argument provides value to parameter
add (5, 3)

#*************************************
## passing String value
def say_hello(name, surname):
    print(f"Hello, {name} {surname}")

say_hello("Bob", "Smith")
# Output: Hello, Bob Smith

#**************************************
## passing String value by argument for each parameter
def say_hello1(name, surname):
    print(f"Hello, {name} {surname}")

say_hello1(surname= "Bob", name= "Smith")
# Output: Hello, Smith Bob


# math argument
def divide(dividend, divisor):
    if divisor!= 0:
        print(dividend/divisor)
    else:
        print("Hello World!")

divide(dividend=15,divisor=3) 