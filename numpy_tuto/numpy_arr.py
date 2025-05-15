import numpy as np

arr = np.array([[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14]])

# Transpose the array

transpose_arr = np.transpose(arr)

print("Original array:")
print(arr)

print("\nTranspose array:")

print(transpose_arr)

# Calculate the sum of each row

row_sums = np.sum(arr, axis=1)

print("\nSum of each row:")

print(row_sums)

# Calculate the sum of each column

column_sums = np.sum(arr, axis=0)

print("\nSum of each column:")

print(column_sums)