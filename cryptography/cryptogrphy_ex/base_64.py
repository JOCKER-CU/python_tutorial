import base64

message = "HelloWorld".encode("ascii")

encoded_message = base64.b64encode(message)
decoded_message = base64.b64decode(encoded_message)
print("Original message:", message.decode("ascii"))
print("Encoded message:", encoded_message)
