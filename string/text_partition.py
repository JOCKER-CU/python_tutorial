# 8. Miscellaneous
# str.partition(separator): Splits the string at the first occurrence of the separator and returns a tuple.
# str.center(width): Centers the string within the specified width, padding with spaces by default.
# str.ljust(width): Left-aligns the string within the specified width.
# str.rjust(width): Right-aligns the string within the specified width.


text="Hello, World!"
text_partition = text.partition(',')
print(text_partition)

# center 
text_center = text.center(20)
print(f"center : {text_center}")

# ljust()
text_left = text.ljust(20)
print(f"left-align : '{text_left}'")

# rjust()
text_right = text.rjust(29)
print(f"right-align : '{text_right}'")

a = 'a'
b = 'b'
print(a> b)
print(ord(a), ord(b), sep="\n")
name= 'Han Naung Soe'
print(f'multipyl by string and numbe, {name * 4}', end='\n')

print(f'find word in string : {'Han' in name}')
