import random
import time

print(
    """
===========================================================
****** Welcome to the Advanced Number Guessing Game ******
===========================================================
Please enter an integer between 1 and 100.
"""
)

number = random.randint(1, 100)

attempts = 0

name = input("Enter your name: ")
print(f"Hello, {name}! Let's play the game.")

while attempts < 5:
    try:
        guess = int(input(f"Attempt {attempts + 1}: "))
        attempts += 1
        guessleft = 5 - attempts
        print("Checking your guess...")
        time.sleep(1)

        if guess < number:
            print("Too low! Try again. You have", guessleft, "guess(es) left.")
            time.sleep(1)
        elif guess > number:
            print("Too high! Try again. You have", guessleft, "guess(es) left.")
            time.sleep(1)
        else:
            print(f"Congratulations, {name}! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")
   
    

    


