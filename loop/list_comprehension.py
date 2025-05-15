#list Comprehension

import time


my_list = [i for i in range(10)]
print(my_list)

# Nested list comprehension

nested_list = [[i for i in range(5)] for j in range(5)]
print(nested_list)

even_numbers = [i for i in range(10) if i % 2 == 0]
print("Even numbers in the range are:", even_numbers)

odd_numbers = [i for i in range(10) if i % 2!= 0]

print("Odd numbers in the range are:", odd_numbers)

# Dictionary comprehension

my_dict = {i: i**2 for i in range(10)}
print(my_dict)

# Set comprehension

my_set = {i for i in range(10) if i % 2 == 0}
print(my_set)

# Generator expression

my_generator = (i for i in range(10))
print(my_generator, type(my_generator), "which is a generator object")

for i in my_generator:
    print(i, end=" ", flush=True)
    time.sleep(1)