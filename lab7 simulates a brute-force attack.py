# Write a Python program that simulates a brute-force attack on a password by trying out
# allpossible character combinations

import string
import itertools

chars = string.digits
password = '123'
max_length = len(password)

for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        candidate  = "".join(combination)
        print("tryping password: " + candidate)

        if candidate == password:
            print("password found:", candidate)
            raise SystemExit
