#class method

class MyClass:
    name = 'myclass'
    def __init__(self):
        self.name = "MyClass"

    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.name}"
    
    @staticmethod
    def static_method():
        return "This is a static method"

my_obj = MyClass()

print(MyClass.class_method())  # Output: This is a class method of MyClass

print(my_obj.class_method())  # Output: This is a class method of MyClass

print(MyClass.static_method())  # Output: This is a static method

print(my_obj.static_method())  # Output: This is a static method