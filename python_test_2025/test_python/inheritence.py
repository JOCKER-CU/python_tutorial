

#inheritence of this clss

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old')

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def introduce(self):
        print(f'Hi, my name is {self.name} and I am {self.age} years old and my roll number is {self.roll_no}')

#creating object of Student class
s1 = Student('Alice', 22, 101)

#calling introduce method

s1.introduce()