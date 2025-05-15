
#lambda function to check if a number is prime

is_prime = lambda num: all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print(is_prime(17))  # Output: True

#lambda function to calculate the factorial of a number

factorial = lambda num: 1 if num == 0 else num * factorial(num-1)
print(factorial(5))  # Output: 120