#lab program no 6
# Write a Python program that reads a file containing a list of usernames and passwords,
# one pairper line (separatized by a comma). It checks each password to see if it has been
# leaked in a databreach. You can use the "Have I Been Pwned" API
# (https://haveibeenpwned.com/API/v3) tocheck if a password has been leaked

import requests
import hashlib

with open('passwd1.txt','r')as f:
    for line in f:

        username,password=line.strip().split(',')

        password_hash=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

        response=requests.get(f"https://api.pwnedpasswords.com/range/{password_hash[:5]}")

        if response.status_code == 200:

            hashes=[line.split(':')for line in response.text.splitlines()]

            for h,count in hashes:

                if password_hash[5:] ==h:
                    print(f"password for user {username} has been leaked {count} times")
                    break
        else:
            print(f"could not check password for user {username}")
