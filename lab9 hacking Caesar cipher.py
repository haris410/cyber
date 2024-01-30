#lab program number 9
# 9 Python program implementation for hacking Caesar cipher algorithm


def shift_letter(letter, amount):
    letter = letter.upper()
   
    code = ord(letter)
   
    if code >= 65 and code <= 90:
        code = code + amount
        if code > 90:
            code = code - 26
        elif code < 65:
            code = code + 26
        letter = chr(code)
    return letter


def decrypt(message, shift):
    plaintext = ""
    for letter in message:
       plaintext = plaintext + shift_letter(letter, -shift)
    return plaintext


message = input("Enter cipher text:")
for shift in range(1, len(message)):
    
    plaintext = decrypt(message, shift)
    
    print("Shift:", shift, "Plaintext:", plaintext)