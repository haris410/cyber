# 11 Python program for encoding and decoding using Base64


import base64

def base64_encode(text):
    encode_bytes = base64.b64encode(text.encode('utf-8'))
    encode_text = encode_bytes.decode('utf-8')
    return encode_text

def base64_decode(encode_text):
    decode_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decode_bytes.decode('utf-8')
    return decoded_text


text_to_encode = "hello, Base64 Encoding and Decoding !"
encoded_text = base64_encode(text_to_encode)
print("Encoded Text :", encoded_text)
decoded_txt = base64_decode(encoded_text)
print("Decoded Text :", decoded_txt)