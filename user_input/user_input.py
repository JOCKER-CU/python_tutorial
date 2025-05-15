# User input function examples

# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Input with type conversion
age = int(input("Enter your age: "))
print(f"In 5 years, you'll be {age + 5} years old.")

# Input with validation
while True:
    try:
        height = float(input("Enter your height in meters: "))
        if height > 0:
            break
        else:
            print("Height must be a positive number.")
    except ValueError:
        print("Please enter a valid number.")
print(f"Your height is {height} meters.")

# Multiple inputs
first_name, last_name = input("Enter your first and last name (separated by space): ").split()
print(f"Your full name is {first_name} {last_name}.")

# Input with default value
favorite_color = input("Enter your favorite color (press Enter for default 'blue'): ") or "blue"
print(f"Your favorite color is {favorite_color}.")

# Password input (hiding characters)
import getpass
password = getpass.getpass("Enter your password: ")
print("Password received (not shown for security)", password)

# Multiline input
print("Enter a short story (press Enter twice to finish):")
story_lines = []
print("Enter a short story (press Enter twice to finish):")
story_lines = []
while True:
    line = input()
    if line:
        story_lines.append(line)
    else:
        break
story = "\n".join(story_lines)
print("\nYour story:")
print(story)
print("\nYour story:")
print(story)

# Input with choices
print("\nChoose a fruit:")
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, 1):
    print(f"{i}. {fruit}")

while True:
    choice = input("Enter the number of your choice: ")
    if choice.isdigit() and 1 <= int(choice) <= len(fruits):
        chosen_fruit = fruits[int(choice) - 1]
        print(f"You chose {chosen_fruit}.")
        break
    else:
        print("Invalid choice. Please try again.")

# Confirmation input
confirmation = input("Do you want to proceed? (y/n): ").lower()
if confirmation in ['y', 'yes']:
    print("Proceeding...")
else:
    print("Operation cancelled.")