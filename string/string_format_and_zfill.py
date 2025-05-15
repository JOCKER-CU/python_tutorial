# 6. Formatting
# str.format(*args, **kwargs): Formats the string using placeholders {}.
# str.zfill(width): Pads the string on the left with zeros to reach the specified width.
format_string= "My name is {}, I am {} years old, I live in {}".format("Han Naung Soe", '23', 'Yangon')
print(format_string)

format_next_string = 'Hello {name}, Welcome to {lan}'.format(name = "Bob", lan = 'JavaScript')

print(format_next_string)

age = '25'
padd_age = age.zfill(5)
print(padd_age)