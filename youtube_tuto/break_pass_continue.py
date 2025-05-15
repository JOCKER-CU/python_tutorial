# while True:
#     try:
#         # Prompt user for directory path
#         directory_path = input("Enter the path to the directory: ")

#     except:
#         print("Invalid input. Please enter a valid directory path.")
#         continue;

phone_no = "1234-5678-90"
no = ""
for i in phone_no:
    if i == "-":
        print("Found a hyphen")
        continue;
    no += i;
print(no)

