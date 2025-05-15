import numpy as np

arr = np.array([0, 1, 2, 3, 4])

x = arr.view()

x[0] = 5

print("Original array:", arr)

print("View array:", x)