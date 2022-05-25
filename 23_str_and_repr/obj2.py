class Person:
    def __init__(self, name, age):
        self.name = name    
        self.age = age

    def __str__(self):  ## str method is called when we want to return object into a string
        return f"Person {self.name}, {self.age} years old."
    
    def __repr__(self):  ## repr method is called to print out unambiguous representation of an object
        return f"<Person({self.name}, {self.age})>"

bob = Person("Bob", 35)
print(bob)