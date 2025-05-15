
def add_numbers(a, b):
    return a + b;

def subtract_numbers(a, b):
    return a - b;

def multiply_numbers(a, b):
    return a * b;

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed.";
    else:
        return a / b;

def calculate_modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero is not allowed.";
    else:
        return a % b;

def calculate_power(a, b):
    return a ** b;

def calculate_factorial(n):
    if n == 0:
        return 1;
    else:
        return n * calculate_factorial(n - 1);

def calculate_fibonacci(n):
    if n <= 0:
        return "Error: Input must be a positive integer.";
    elif n == 1:
        return 0;
    elif n == 2:
        return 1;
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b;
