# With a string
name = "OpenAI"
print("O" in name)        # True
print("X" in name)        # False

# With a list
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)       # True
print(6 in numbers)       # False
print(not 7 in numbers)  # True

# With a dictionary (checks only keys)
info = {"name": "Alice", "age": 25}
print("name" in info)     # True
print("address" in info)  # False
