
file = open('file_handling\example.txt');

print(file.read())
file.write("ehllo")
with open('file_handling/example.txt', 'r') as file:
    print(file.read())

# Open the file for appending
with open('file_handling/example.txt', 'a') as file:
    file.write("ehllo\n")


# No need to explicitly close the file when using 'with' statement))
file.close()

