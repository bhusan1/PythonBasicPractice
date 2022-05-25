class ClassTest:
## instance method gets the object/instance 
## when you want to produce an action that uses data inside the object 
    def instance_method(self):
        print(f"Called instance_method of {self}")

## class method gets the class passed
## used often as factories
    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

## static method doesn't get anything passed
## to place a method inside a class to make sense logically
    @staticmethod
    def static_method():
        print("Called static_method.")



ClassTest.class_method()
ClassTest.static_method()

#test.instance_method()