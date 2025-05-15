# print("Han Naung Soe")

import math


x = 20
y = 40

z = x + y
u = x * y

print(u)

print(z)

# float
pi = 3.14

# String 
name = "Mg Mg"

# boolean
is_student = True

# Arithematic operators
sum = 10 + 5
difference = 10 - 5
product = 10 * 5
quotient = 10 / 5

print(sum)
print(difference)
print(product)
print(quotient)

# Comparison operators
is_equal = (10 == 5)  #equal to 
is_greater = (10 > 5) #Greater than

print(is_equal)
print(is_greater)

# Logical operators
logical_and = (True and False)
logical_or = (True or False)

print(logical_and)
print(logical_or)

#If-else statements 
age = 13
if age > 18 :
    print('Adult')
else:
    print("Minor")

# For loops
for i in range(5):
    print(i)

# while loops

count = 0;
while count < 5:
    print(count)
    count += 1


# Functions

def greet(name):
    return f"hello, {name}!"

print(greet("Alice"))

# List
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple

for i in fruits:
    print(i)


# Dictionary
person = { "name" : "John", "age" : 30}
print(person["name"], person["age"])

print(math.sqrt(16))

# triple quoted string

param = """ What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of 
the printing and typesetting industry. 
Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s
, when an unknown printer took a galley 
of type and scrambled it to make a type 
specimen book. It has survived not only
 five centuries, but also the leap into 
 electronic typesetting, remaining essentially 
 unchanged. It was popularised in the 1960s with the release of Letraset sheets 
 containing Lorem Ipsum passages, and more recently with desktop publishing software
 like Aldus PageMaker including versions of Lorem Ipsum
"""

print(param)

total = 1 + 2 + 3 + \
    4 + 5 + 6 +\
          7 + 8 + 9 

print(total)




