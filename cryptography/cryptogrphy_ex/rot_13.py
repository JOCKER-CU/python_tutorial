# ROT13
message = "HelloWorld"


def encrypt(col_size, message):
    ciphertext = [""] * col_size
    print("Ciphertext:", ciphertext)

    for col in range(col_size):
        pointer = col
        print("Pointer:", pointer)
        print("len(message):", len(message))
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            print("Message[pointer]:", message[pointer])
            print("Ciphertext[col]:", ciphertext[col])
            pointer += col_size
            print("Pointer:", pointer)
            print("Ciphertext:", ciphertext)
            print()



    return "".join(ciphertext)            

print(encrypt(2, message))