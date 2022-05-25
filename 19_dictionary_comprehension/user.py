users=[
    (0, "Bob", "password"),
    (1, "Rolf", "wordpass"),
    (2, "Jose", "passsing123"),
    (3, "Kat", "1234"),
]

# dictionary comprehension
username_mapping = {user[1]: user for user in users}
print(username_mapping)
#Output: {'Bob': (0, 'Bob', 'password'), 'Rolf': (1, 'Rolf', 'wordpass'), 'Jose': (2, 'Jose', 'passsing123'), 'Kat': (3, 'Kat', '1234')}


username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!!")