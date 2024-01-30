#lab program number 3
#  Write a Python program to check if a password meets the following criteria:
# a. At least 8 characters long,
# b. Contains at least one uppercase letter, one lowercase letter, one digit, and one special
#     character (!, @, #, $, %, or &),
# c. If the password meets the criteria, print a message that says "Valid Password." If it
#     doesn'tmeet the criteria, print a message that says "Password does not meet requirements."

import re

def validate(password):
        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()]).{8,}$"
        
        if bool(re.match(pattern, password)):
            print(password ,"password is valid")
        else:
            print(password ," password is invalid")
password=input("Enter password:")           
validate(password)