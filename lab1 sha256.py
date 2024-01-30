# Write a Python program that defines a function and takes a password string as input and
# returnsits SHA-256 hashed representation as a hexadecimal string.

import hashlib

string = "hello world"

string = string.encode("utf-8")
object = hashlib.sha256(string)
hexa_digest = object.hexdigest()

print(hexa_digest)