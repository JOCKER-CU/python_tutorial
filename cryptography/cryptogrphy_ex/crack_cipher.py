message = "ugetgv"

LETTERS = "abcdefghijklmnopqrstuvwxyz"

for key in range(len(LETTERS)):
    print("Trying key %s" % key)
   

    translated = ""
    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = (num - key)
            print(num) 
            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol
    print("Key %s: %s" % (key, translated))
    print()
            

