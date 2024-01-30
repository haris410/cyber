#lab program no 2

# Write a Python program that defines a function to generate random passwords of a
# specifiedlength. The function takes an optional parameter length,
# which is set to 8 by default. If no lengthis specified by the user, the password will have 8 characters.

import random
import string
def generate_password(length=8):
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_characters)
        for i in range(length))
    return password

password_length_str = input("input the desired lenght of password :")
if password_length_str:
    password_lenght = int(password_length_str)
else:
    password_lenght = 8

password = generate_password(password_lenght)
print(f"generated password is: {password}")

                        