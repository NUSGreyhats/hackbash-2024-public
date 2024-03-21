#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from random import randbytes, choice

def print_blocks(ct):
    for i in range(0,len(ct),32):
        print(ct[i:i+32])

def chal():
    key = randbytes(16)
    iv = randbytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pw = randbytes(16).hex()
    email = f"Hi everyone!\nThe last email was badly encrypted. Instead now the details are in a encrypted zip file. The password is {pw}. Please dont share the password!"
    enc = cipher.encrypt(pad(email.encode(),16)).hex()
    print("They caught on to our attack and now no longer provides the encryption service! However we seem to have gotten some side channel working...")
    print(f"Email:")
    print_blocks(enc)
    for _ in range(16*32):
        ct = bytes.fromhex(input("Ciphertext (in hex): "))
        if ct == b"DONE":
            break
        try:
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct),16)
            print("Decryption successful")
        except:
            print("Decryption failed")
    print("Can you tell us the password?")
    assert input("password: ")==pw
    flag = open("flag","r").read()
    print(f"Here you go: {flag}")

chal()
