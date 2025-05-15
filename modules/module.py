#modules

import math
import random
import string
import time

# string

text = "Hello, World!"
text_lower = text.lower()
text_upper = text.upper()
text_prefix = "H"
text_suffix = "!"

# type of string

print(f"{text_lower}.islower: {text_lower.islower()}")
print(f"{text_upper}.isupper(): {text_upper.isupper()}")
print(f"{text_prefix}.startswith(): {text_prefix.startswith('H')}")
print(f"{text_suffix}.endswith: {text_suffix.endswith('.')}")

# splitting and joining

text = "apple,orange,mangoe,cherry"
split_text = text.split(',')
print(split_text)
print(type(split_text))

text = "Hello\nWorld\nPython"

split_lines = text.splitlines()

print(split_lines)
print(type(split_lines))

join_text = " ".join(split_lines)

print(join_text)
                 