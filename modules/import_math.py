
import math

print(math.sqrt(25))  # Output: 5.0
print(dir(math))  # Output: ['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan

print(math.pi)  # Output: 3.141592653589793

print(math.e)  # Output: 2.718281828459045

print(math.sin(math.pi / 2))  # Output: 1.0

print(math.cos(math.pi / 2))  # Output: 6.123233995736766e-17

print(help(math.sqrt))  # Output: Help on built-in function sqrt in module math:)

print(math.sqrt(16))            # Output: 4.0

import random
print(random.randint(1, 10))    # Output: Random integer between 1 and 10


import requests

response = requests.get('https://api.github.com/users/octocat')

print(response.json())  # Output: Dictionary containing user information
