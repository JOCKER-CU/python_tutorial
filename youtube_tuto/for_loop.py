import time

# First loop - Print characters and their ASCII values
text = "Jocker CU"
for char in text:  # Using 'char' instead of 'i' for better clarity
    print(char)
    print(f"ASCII value: {ord(char)}")  # Added label for clarity
    print("--------")
    time.sleep(1)

print("Happy Day!")

# Second loop - Print numbers from 50 to 99
for num in range(50, 100):  # Using 'num' instead of 'i' for better clarity
    print(num)
    print("--------")
    time.sleep(0.1)
    
