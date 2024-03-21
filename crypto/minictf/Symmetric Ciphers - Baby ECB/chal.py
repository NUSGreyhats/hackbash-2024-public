#!/usr/local/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from random import randbytes, choice

def print_blocks(ct):
    for i in range(0,len(ct),32):
        print("\t"+ct[i:i+32])

def chal():
    key = randbytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    fruit = choice("lemon mango peach kiwis pines dates apple berry guava plums".split())
    month = choice("Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())
    day = choice(range(1,10))
    email = f"Hi everyone!\nThe plan is to hunt down every {fruit} we can find anywhere on the {day} of {month}!"
    enc = cipher.encrypt(pad(email.encode(),16)).hex()
    print("We interrupted a suspicious email, can you help us decrypt it and prevent the attack?")
    print(f"Email:")
    print_blocks(enc)
    for _ in range(111):
        pt = input("Plaintext: ")
        if pt == "DONE":
            break
        ct = cipher.encrypt(pad(pt.encode(),16)).hex()
        print(f"Ciphertext:")
        print_blocks(ct)
    print("Can you tell us the details?")
    assert input("fruit: ")==fruit
    assert input("month: ")==month
    assert int(input("day: "))==day
    flag = open("flag","r").read()
    print(f"Here you go: {flag}")

chal()

