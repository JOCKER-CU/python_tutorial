import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])

# Slicing the array
print(a[1:5]) # [2 3 4 5]
print(a[::2]) # [ 1  3  5  7  9 11 13]

print(a[4::]) # [ 5  6  7  8  9 10 11 12 13]

print(a[:4]) #[1 2 3 4]

print(a[-3:-1]) #[11 12]

print(a[1:5:2]) #[2 4] [start,end,step]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4]) # [7 8 9] 

print(arr[0:2, 2]) # [3 8]

print(arr[0:2, 1:4]) # [[2 3 4] [7 8 9]]