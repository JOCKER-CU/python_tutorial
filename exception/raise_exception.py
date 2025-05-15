 # raise a custom exception

class MyException(Exception):
     pass

def raise_custom_exception():
     raise MyException("Custom exception raised.")

try:
     raise_custom_exception()
except MyException as e:
     print(f"Caught custom exception: {e}")
     # You can add additional error handling or logging here
finally:
     print("This block always executes, regardless of whether an exception occurred.")

print("Program continues after exception handling.")


def check_positive_number(num):
     if num > 0:
         return True
     else:
         raise ValueError("Number must be positive.");

try:
    #  number = int(input("Enter a positive number: "))
     number = 5;
     if check_positive_number(number):
         print("Number is positive.")
     else:
         print("Number is not positive.");
except ValueError as e:
     print(f"Caught value error: {e}")


# raising an exception using try-except block
print("+" *50 , "\n")
class NegativeNumberError(Exception):
     pass

def check_negative_number(num):
     if num < 0:
         raise NegativeNumberError("Number is negative.")
     return num

try:
     print(check_negative_number(-5));
except NegativeNumberError as e:
     print(f"Caught negative number error: {e}")


print("+" *50 , "\n")
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Caught a division by zero error.")
        raise  # Re-raises the original ZeroDivisionError

try:
    divide(5, 0)
except ZeroDivisionError as e:
    print(f"Error re-raised: {e}")
