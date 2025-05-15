# 4. Checking Types
# str.isalpha(): Returns True if all characters in the string are alphabetic.
# str.isdigit(): Returns True if all characters in the string are digits.
# str.isalnum(): Returns True if all characters in the string are alphanumeric.
# str.isspace(): Returns True if all characters in the string are whitespace.
# str.islower(): Returns True if all characters in the string are lowercase.
# str.isupper(): Returns True if all characters in the string are uppercase.
# str.startswith(prefix): Returns True if the string starts with the specified prefix.
# str.endswith(suffix): Returns True if the string ends with the specified suffix.

# Example strings
text_alpha = "Hello"
text_digit = "12345"
text_alnum = "Hello123"
text_space = "   "
text_lower = "hello"
text_upper = "HELLO"
text_prefix = "Hello, World!"
text_suffix = "Welcome to Python."

# all chars in the string are alphabetic
print(text_alpha.isalpha())
print(f"{text_alpha}.isalpha(): {text_alpha.isalpha()}")

# all chars in the string are digit
print(f"{text_digit}.isDigit(): {text_digit.isdigit()}")

# all chars are in the string are alphanumric
print(f"{text_alnum}.isalnum: {text_alnum.isalnum()}")

# all chars are in the string are whitespace
print(f"{text_space}.isspace(): {text_space.isspace()}")

# all  chars are in the string are lower case
print(f"{text_lower}.islower: {text_lower.islower()}")

# all chars are in the string are uppercase
print(f"{text_upper}.isupper(): {text_upper.isupper()}")

# all chars are in the string are starting with the specified prefix.
print(f"{text_prefix}.startswith(): {text_prefix.startswith('H')}")

# all chars are in the string are ending with the specified suffix
print(f"{text_suffix}.endswith: {text_suffix.endswith('.')}")