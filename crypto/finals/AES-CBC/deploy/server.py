from Crypto.Cipher import AES
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Util.Padding import pad
import os

allowed_chars = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

flag = b"flag{dont_use_aes_cbc_with_a_predictable_iv}" # Omitted
assert len(set(flag) - set(allowed_chars)) == 0
key = os.urandom(16)
iv = bytes_to_long(os.urandom(16))

def encrypt_data(data:str):
    global iv; iv = (iv + 1) & ((1<<128) - 1)
    data = b"data=" + bytes.fromhex(data) + b",flag=" + flag
    data = pad(data, 16)
    biv = long_to_bytes(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv=biv)
    return (biv + cipher.encrypt(data)).hex()

while True:
    data = input("Input (hex): ")
    print("Output (hex): ", encrypt_data(data))