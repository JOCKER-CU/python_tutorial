# 5. Splitting and Joining
# str.split(separator): Splits the string into a list at each occurrence of the separator.
# str.rsplit(separator): Splits the string into a list at the last occurrence of the separator.
# str.splitlines(): Splits the string at line breaks and returns a list.
# str.join(iterable): Joins elements of an iterable (e.g., list) with the string as a separator.

text = 'apple,orange,mangoe,cherry'
text_with_line = 'Hello\nWorld\nPython'
words_list = ['Hello', 'World', 'Python']

# split()
split_text= text.split(',')
print(split_text)

# rsplit()
rsplit_text = text.rsplit(',',1)
print(rsplit_text)

# splitlines()
split_newlines = text_with_line.splitlines()
print(split_newlines)

# join()
join_text = ' '.join(words_list)
print(join_text)


