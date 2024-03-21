#!/usr/bin/python3
from hashlib import sha256
from os import urandom

secret = urandom(20)
data = b"admin=True"
msg = secret+data
h = sha256(msg).hexdigest()
tail = b"&admin=False"

print(f"{h = }")
h = input("h = ")
nmsg = bytes.fromhex(input("nmsg = "))

assert h == sha256(secret+nmsg).hexdigest()
assert nmsg[:len(data)] == data
assert nmsg[-len(tail):] == tail

with open("flag","r") as f:
    print(f.read())
