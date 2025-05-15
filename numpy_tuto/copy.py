import numpy as np

arr = np.array([0, 1, 2, 3, 4])

x = arr.copy()

x[0] = 10

print("Original array:", arr)

print("Copied array:", x)