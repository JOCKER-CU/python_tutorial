#filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

#reduce

from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
product = reduce(operator.mul, numbers)
plus = reduce(operator.add, numbers)
minus = reduce(operator.sub,numbers)

print(minus)

print(plus)

print(product)

colors = ["Green", "", "Red", "Yellow", "Black", "", "White", "", "Pink",  "Orange"]

filtered_colors = list(filter(None, colors))

print(filtered_colors)

print(colors)

