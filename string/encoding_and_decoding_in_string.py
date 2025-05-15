# 7. Encoding and Decoding
# str.encode(encoding='utf-8'): Encodes the string into bytes using the specified encoding (default is UTF-8).
# str.decode(encoding='utf-8'): Decodes bytes to a string using the specified encoding.

text = 'Hello Python!'
encoded_str = text.encode('utf-8')
print(f"Encoded: {encoded_str}")

decoded_str = encoded_str.decode('utf-8')
print(f"Decoded: {decoded_str}")