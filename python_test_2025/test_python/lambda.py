x = lambda x: x + 10

print(x(5))

x = lambda a, b : a * b

print(x(5, 6))

x = lambda a, b, c : a + b + c

print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def trifunc(b,c):
  return lambda a : a * b * c

myTriple = trifunc(2,3)

print(myTriple(5))