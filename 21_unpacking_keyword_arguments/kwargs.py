# kwargs does dictionary unpacking with keyword arguments

# collect named arguments into a dictionary
def named(**kwargs):
    print(kwargs)

named(name="Bob", age = 25)
#Output: {'name': 'Bob', 'age': 25} || keyword arguments get collected in kwargs variable


# unpack a dictionary into named arguments
def named1(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}

named1(**details)
# output: Bob 25



# post function for REST API also uses kwargs
'''
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
'''