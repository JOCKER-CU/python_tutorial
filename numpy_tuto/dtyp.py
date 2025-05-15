import numpy as numpy

arr = numpy.array([0, 1, 2, 3, 4])

print("Type", arr.dtype)


fruit = numpy.array(["apple", "banana", "cherry"])

print("Type", fruit.dtype)

a = numpy.array([1, 2, 3, 4], dtype='S')

print("Type", a.dtype)


b = numpy.array([1, 2, 3, 4], dtype='i4')

print("Type", b.dtype)

c = numpy.array([1, 2, 3, 4], dtype='f8')

print("Type", c.dtype)

d = numpy.array([1+2j, 3+4j, 5+6j])

print("Type", d.dtype)