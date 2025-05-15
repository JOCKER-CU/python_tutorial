#Magic Method 

   
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"My name is {self.name}, I am {self.age} years old"
    
    def __add__(self, other):
        return MyClass(self.name + other.name, self.age + other.age)
    
person1 = MyClass("Alice", 25)

print(person1)  # Output: My name is Alice, I am 25 years old

person2 = MyClass("Bob", 30)

person3 = person1 + person2

print(person3)  # Output: My name is AliceBob, I am 55 years old


#Special Method

class MyItems:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
my_items = MyItems(["apple", "banana", "cherry"]);
print("=" * 30)
print(len(my_items))  # Output: 3

print(my_items[0])  # Output: apple


