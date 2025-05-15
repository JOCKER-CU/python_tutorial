#zip function

# Create two lists of numbers

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]

# Use the zip function to pair corresponding elements

zipped_numbers = list(zip(numbers1, numbers2))

print(zipped_numbers)

# Unzip the zipped numbers

numbers1_unzipped, numbers2_unzipped = zip(*zipped_numbers)

print(f"Unzipped numbers1: {numbers1_unzipped}")
print(f"Unzipped numbers2: {numbers2_unzipped}")