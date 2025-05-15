
x = 5
print(id(x))
x = x + 1
print(id(x))
y = x 
print(id(y))

print( x == y)

x = 5
while x <= 200:
    print(x)
    x += 1