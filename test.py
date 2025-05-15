i = 20
name = "Han Naung Soe"

print(i);
print(f'My name is {name}!, I am {i} years old.');

# List

numbers = [1, 2, 3, 4, 5]
print(numbers[2]);

# Dictionary

person = {
    'name': 'Han Naung Soe',
    'age': 25,
    'city': 'Yangon'
},{
    'name': 'Alice',
    'age': 30,
    'city': 'Tokyo'
},{
    'name': 'Bob',
    'age': 35,
    'city': 'Seoul',
    'city': 'New York'
}

for p in person:
    print(p['name'], p['age'], p['city'] + '\n');


# print(person['name']);
# print(person['city']);
person[0]['city'] = 'London'
print(person)

# Tuple

coordinates = (10, 20)
programming_languages = ('Python', 'JavaScript', 'C++', 'Java','Go');

for language in programming_languages:
    print(language ,);
print(coordinates[0]);

# Set

fruits = {'apple', 'banana', 'cherry'}
print(fruits.add('orange'));
for fruit in fruits:
    print(fruit);

# Function

def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"));

# Class and Object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 25)

print(person1.name);
print(person1.age);

