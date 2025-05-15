#lambda

double = lambda x: x * 2;

#functions
print(double(4))

#lambda

double = lambda x: x * 2

#functions
print(double(4))

add = lambda a, b: a + b

#functions

print(add(3, 5))

#lambda
subtract = lambda x, b: x - b;

#functions

print(subtract(10, 5))

multiply = lambda x, b: x * b

#functions 

print(multiply(5, 6))

divide = lambda x, b: x / b

#functions

print(divide(10, 2))

#modulus

modulus = lambda x, b: x % b

#functions

print(modulus(10, 3))

#power

power = lambda x, b: x ** b

#functions

print(power(2, 3))

#factorial

factorial = lambda x: 1 if x == 0 else x * factorial(x-1)

#functions

print(factorial(5))

#fibonacci

fibonacci = lambda n: 0 if n <= 0 else 1 if n == 1 else fibonacci(n-1) + fibonacci(n-2)

#functions

print(fibonacci(10))

#list

numbers = [1, 2, 3, 4, 5]

#functions
print(list(map(lambda x: power(x,3),numbers)))

numberslist = list(range(1,11));
print(numberslist)

print(list(map(lambda x: x ** 2, numberslist)))