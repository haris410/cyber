#lab program number 10
# 10 Python program to implement asymmetric encryption using rsa python library


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

KeyP=RSA.generate(3072)

pubK=KeyP.public_key()
pubKeyPEM=pubK.exportKey()

privKeyPEM=KeyP.exportKey()

#encryption
msg=b' How are you '
encryptor=PKCS1_OAEP.new(pubK)
encrypted=encryptor.encrypt(msg)
print("Encrypted message:",binascii.hexlify(encrypted))

decryptor=PKCS1_OAEP.new(KeyP)
decrypted=decryptor.decrypt(encrypted)
print("Decrypted message:",decrypted.decode('utf-8'))

