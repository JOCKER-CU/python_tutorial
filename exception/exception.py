
#exception handling using try-except block

def divide_numbers(x, y):
    try:
        result = x / y
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    except TypeError:
        print("Error: Invalid input type. Please provide numeric values.")
        result = None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        result = None
    finally:
        print("Division operation completed.")
        return result  # Return the result, whether it’s a value or None

# Testing the function with various inputs

result1 = divide_numbers(10, 2)  # Expected: 5.0
result2 = divide_numbers(5, 0)   # Expected: Error message for division by zero
result3 = divide_numbers("10", 2) # Expected: Error message for invalid input type
result4 = divide_numbers(10, "2") # Expected: Error message for invalid input type
result5 = divide_numbers(10, None) # Expected: Error message for invalid input type


try:
    num1 = int('ab234');
    num2 = int('34t')
    print(f'the result is: {num1 + num2}')

except ValueError:
    print("Invalid input. Please enter numeric values.")
except:
    print("An unexpected error occurred.")
print("Program execution completed.")