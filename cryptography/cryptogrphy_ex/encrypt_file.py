from cryptography.fernet import Fernet


key = Fernet.generate_key()
print(key)

with open("secretKey.key", "wb") as key_file:
    key_file.write(key)

with open("secretKey.key", "rb") as key_file:
    key = key_file.read()

print(key)
cipher_suite = Fernet(key)

with open("7.1 example.csv", "rb") as file:
    file_data = file.read()
    print(file_data)

encrypted_data = cipher_suite.encrypt(file_data)
print(encrypted_data)
with open("encrypted_file.csv", "wb") as file:
    file.write(encrypted_data)