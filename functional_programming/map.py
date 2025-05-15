#map

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

#filter 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
odd_numbers = list(filter(lambda y: y % 2 != 0, numbers))
print(odd_numbers)

#reduce

from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
product = reduce(operator.mul, numbers, 1)

print(product)