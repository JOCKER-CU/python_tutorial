
password = "Password_@123"

if len(password) < 8:
    print("Password must be at least 8 characters long.")
    exit();
if not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
    exit();

if not any(char.isalpha() for char in password):
    print("Password must contain at least one letter.")
    exit();

if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
    exit();

if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
    exit();

if not any(char in "!@#$%^&*()" for char in password):  
    print("Password must contain at least one special character.")
    exit()
else:
    print("Password is valid.")
    