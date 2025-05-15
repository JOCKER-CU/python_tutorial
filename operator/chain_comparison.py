#chain comparison operators

print(10 > 5 and 10 < 15)  # True

print(10 > 15 or 10 < 5)  # False

print(10 == 10)  # True

print(10 != 10)  # False

#chain logical operators

print((True and False) or True)  # True

print(True and (False or True))  # True

print((True and False) or (False and True))  # False

#chain comparison and logical operators

print(10 > 5 and 10 < 15 or True)  # True

print(10 > 5 and (10 < 15 or True))  # True

print((10 > 5 and 10 < 15) or True)  # True

print((10 > 5 and 10 < 15) or (True and False))  # True

print(10 > 5 and 10 < 15 or True and False)  # True