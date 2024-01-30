#lab program no 8
# Python program for implementation symmetric encryption using Caesar cipher algorithm

def c_s(text,shift):
    en_text=" "
    for char in text:
        if char.isalpha():
            s_char=chr(ord(char)+shift)
            en_text+=s_char
        else:
            en_text+=char
    return en_text
p_text=(input("Enter Plain Text:"))
shift=2
 
print("Plain Text =",p_text)
en_text=c_s(p_text,shift)
print(" Encrypted Text =",en_text)
