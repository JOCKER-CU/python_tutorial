#functions in python

def greet(name):
    print(f'Hello, {name}')
    print('%s' % name)

greet('Alice')

#positional functions
def calculate(x, /):
    return x + 10

print(calculate(5, ))

#keyword functions
def calculate(x, *, y):
    return x + y

print(calculate(5, y=10))


#fruits for loop

fruits = ['apple', 'banana', 'cherry']

def loop_fruits(fruits):
    for fruit in fruits:
        print(fruit)

loop_fruits(fruits)

