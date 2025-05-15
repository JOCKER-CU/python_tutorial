class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def introduce(self):
        return f"{self.name} is {self.kind}."
    
    def make_sound(self):
        return "...";
    
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    def sleep(self):
        return f"{self.name} is sleeping."

# Create instances of Animal

dog = Animal("Buddy", "dog")
cat = Animal("Kitty", "cat")

# Call methods

print(dog.introduce())  # Output: Buddy is dog.
print(dog.make_sound())  # Output: ...
print(dog.eat("frisky dog food"))  # Output: Buddy is eating frisky dog food.
print(dog.sleep())  # Output: Buddy is sleeping.