# 3. Whitespace Handling
# str.strip(): Removes leading and trailing whitespace.
# str.lstrip(): Removes leading whitespace.
# str.rstrip(): Removes trailing whitespace.

text= "      Hello World!    "
print(text.strip())


# Remove only leading whitespace using lstrip()
leading_stripped_text = text.lstrip()
print(leading_stripped_text)

# Remove trailing whitesapce using rstrip()
trailing_stripped_text = text.rstrip()
print(trailing_stripped_text)