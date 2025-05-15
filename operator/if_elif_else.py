
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


print("""
      ******* Calculator Menu *******\n\n
  Choose your operation:
 1. Addition
 2. Subtraction
 3. Multiplication
 4. Division
 5. Modulus
 
      """);

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is {result}.")

elif choice == 2:
    result = num1 - num2
    print(f"The difference between {num1} and {num2} is {result}.")

elif choice == 3:
    result = num1 * num2
    print(f"The product of {num1} and {num2} is {result}.")

elif choice == 4:
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"The quotient of {num1} and {num2} is {result}.")

elif choice == 5:
    if num2 == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        result = num1 % num2
        print(f"The remainder of {num1} divided by {num2} is {result}.")
else:
    print("Invalid choice. Please try again.")