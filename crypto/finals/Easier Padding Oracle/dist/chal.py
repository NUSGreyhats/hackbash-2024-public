from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from random import randbytes, choice

key = open("key","rb").read() 
iv = open("iv","rb").read()

def is_valid_pad(ct):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ct)
    try:
        pt = unpad(pt,16)
        return True
    except:
        return False

output = open("output","r").read().strip().split("\n")
pt = b"Here is the flag for the challenge: "
with open("flag","rb") as f: 
    pt += f.read() # your goal is to find out what this is

ct = bytes.fromhex(output[0])
cipher = AES.new(key, AES.MODE_CBC, iv)
assert pt == unpad(cipher.decrypt(ct),16) # the first ciphertext is the flag

for i in output:
    ct = bytes.fromhex(i)
    assert is_valid_pad(ct) # all the ciphertexts have valid padding
