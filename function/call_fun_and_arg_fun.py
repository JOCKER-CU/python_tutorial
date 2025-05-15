
#call funcation and arguments function

# Define call_function_and_arguments to call any passed function with given arguments
def call_function_and_arguments(func, *args, **kwargs):
    return func(*args, **kwargs)

# Define a sample function to call
def greet(name, age):
    return f"Hello, {name}! You are {age} years old."


# Use call_function_and_arguments to call the greet function
# print(call_function_and_arguments(greet, "Alice", 25))  # Output: "Hello, Alice! You are 25 years old."


def calculate_sum(a, b):
    return f'The sum of {a} and {b} is {a + b}.'



def greet(name, age):
    return f"Hello, {name}! You are {age} years old."

# call function
print(greet("Bob", 30));
# return multiple values   

def return_multiple_values():
    return 10, 20, "Alice"

a, b, c = return_multiple_values()
print(a, b, c)



# Transformation functions
def call_function_and_arguments(func, *args, **kwargs):
    return func(*args, **kwargs)

def scale(data, factor):
    return [x * factor for x in data]

def offset(data, amount):
    return [x + amount for x in data]

# Configuration-driven function call
transformations = [
    (scale, ([1, 2, 3],), {"factor": 10}),  # Wrap [1, 2, 3] in a tuple to ensure it's treated as a single positional argument
    (offset, ([10, 20, 30],), {"amount": 5}),
]

# Applying transformations dynamically
for func, args, kwargs in transformations:
    print(call_function_and_arguments(func, *args, **kwargs))
