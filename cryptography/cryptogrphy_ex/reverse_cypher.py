text = "Hello, I am a simple text. I am not encrypted."
transcripted_text = ""

i = len(text) - 1

while i >= 0:
    if text[i] == " ":
        transcripted_text += " "
    else:
        transcripted_text += text[i]
    i -= 1

print(transcripted_text)