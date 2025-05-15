def encryptAndDecryptXOR(key: str, message: str) -> str:
    """
    Encrypts and decrypts a message using XOR cipher with the given key.
    
    :param key: The key used for encryption and decryption.
    :param message: The message to be encrypted or decrypted.
    :return: The encrypted or decrypted message.
    """
    return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))

print("XOR Cipher")
print("Encrypted message:", encryptAndDecryptXOR("key", "Hello World!"))
print("Decrypted message:", encryptAndDecryptXOR("key", encryptAndDecryptXOR("key", "Hello World!")))