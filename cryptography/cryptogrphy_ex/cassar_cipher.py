message = "abcd"

def encrypt(text, amount):
    # Encrypt the text by shifting each letter by the amount
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = (ord(char) - 97 + amount) % 26
            encrypted_text += chr(shift + 97)
        else:
            encrypted_text += char
    return encrypted_text 
 
encrypted_message = encrypt(message, 4)
print("Encrypted message:", encrypted_message)