# calling string variables
name = "Ben" 
location = 'waco'
print (name)
print (location)
# Output: 
# Ben
# waco

#calling string in another variable
new_name = "Hana"
greeting = f'Hello, {new_name}'
print (greeting)
# Output: 
# Hello, Hana

#using template to change name
greet = "Hello, {}"
with_name = greet.format(name)
with_name_two = greet.format("Ram")
print (with_name)
print (with_name_two)
# Output: 
# Hello, Ben
# Hello, Ram

#using template .format for longer phrase
hello = "Hello, {}. Today is {}."
new_Hello = hello.format("Shyam", "Tuesday")
print (new_Hello)
# Output:
# Hello, Shyam. Today is Tuesday.
