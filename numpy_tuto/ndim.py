import numpy as np

a = np.array([42])
b = np.array([1,2,3,4,5,6,7,8,9])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print('a:', a)
print('b:', b)
print('c:', c)
print('d:', d)
print('a.ndim:', a.ndim)
print('b.ndim:', b.ndim)
print('c.ndim:', c.ndim)
print('d.ndim:', d.ndim)
print('a.shape:', a.shape)
print('b.shape:', b.shape)
print('c.shape:', c.shape)
print('d.shape:', d.shape)

print(a[0] + b[2] + c[1,2] + d[1,1,2]);
print(c[1,-1])