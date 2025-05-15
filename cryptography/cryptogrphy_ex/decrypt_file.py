from cryptography.fernet import Fernet

f = Fernet(b'6zyvzo312RDCTzVCQfewJA30pkxLSKmR6zINcGxgw2w=')

with open("encrypted_file.csv", "rb") as file:
    encrypted_data = file.read()
    print(encrypted_data)

decrypted = f.decrypt(encrypted_data)

with open("decrypted_file.csv", "wb") as file:
    file.write(decrypted)
    print("Decrypted: ",decrypted)