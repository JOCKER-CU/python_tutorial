#slicing string
name = "Jocker CU"

print(name[0:3])  # Output: Joc

print(name[3:])  # Output:CKER CU

print(name[3:5])  # Output: CK

print(name[0: : 4])  # Output: Joc

print(name[0:2])

print(name[0:4:2])

reversed_name = name[::-1]
print(reversed_name)

#concatenation

name1 = "Jocker"
name2 = " CU"

concatenated_name = name1 + " " + name2
print(concatenated_name)

#string formatting

name = "Jocker"
age = 30

formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

website = "http://google.com"

slice = slice(7, -4)

print(website[slice])
