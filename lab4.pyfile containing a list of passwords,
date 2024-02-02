#lab program number 4
# Write a Python program that reads a file containing a list of passwords, one per line. It
# checkseach password to see if it meets certain requirements (e.g. at least 8 characters,
# contains bothuppercase and lowercase letters, and at least one number and one special
# character). Passwordsthat satisfy the requirements should be printed by the program.

import re

def validate(password):
        
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()]).{8,}$"
        
        if bool(re.match(pattern, password)):
            print(f"{password} password is valid")
        else:
            print(f"{password} password is invalid")
            
with open("passwd12.txt") as f:
    passwords = f.readlines()
    for password in passwords:
        validate(password.strip())
