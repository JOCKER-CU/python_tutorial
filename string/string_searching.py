# 2. Searching and Replacing
# str.find(substring): Returns the lowest index of the substring if found, otherwise returns -1.
# str.index(substring): Same as find(), but raises a ValueError if the substring is not found.
# str.rfind(substring): Returns the highest index of the substring if found, otherwise returns -1.
# str.replace(old, new): Replaces occurrences of old with new.
# str.count(substring): Returns the number of non-overlapping occurrences of a substring.

text = 'Python Programming is fun!, programming in Python is powerful?'

index_found = text.find("Python")

print(f"Index of 'Python' using find() : {index_found}")


# index()

index_Index = text.index('programming')
print(f'Index of \'programming\' using in index() : {index_Index}')

# rfind()

index_rfind = text.rfind("Python")
print(f"Index of 'Python' using in rfind() : {index_rfind}")

# replace()
replace_of_text = text.replace('Python', 'Java')
print(f"Replacing of 'Python' using replace() : {replace_of_text}")

# count()
count_word = text.count('Python')
print(f"Counting of 'Python' using count() : {count_word} ")

