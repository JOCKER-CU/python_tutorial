import numpy as np

# Create a 2-D array
x = np.arange(15, dtype=np.int64).reshape(3, 5)
x[1:, ::2] = -99

# Find the maximum value per row
max_per_row = x.max(axis=1)

print("Array:\n", x)
print("Max per row:", max_per_row)
