from Crypto.Cipher import DES

def encrypt(key:bytes, plaintext:bytes) -> (bytes, bytes):
    k1, k2 = key[:8], key[8:]
    cipher1 = DES.new(k1, DES.MODE_ECB)
    cipher2 = DES.new(k2, DES.MODE_ECB)
    peek = cipher1.encrypt(m)
    return cipher2.encrypt(peek), peek

flag = b'flag{XXXXXXXXXXXXXXXXXXXXXXXXXXX}' # OMITTED HAHAHA
m = flag + b"\0" * ((-len(flag)) % 8)

key = b'XXXXXXXXXXXXXXXX' # OMITTED HAHAHA
c, peek = encrypt(key, m)
assert m == c

print("peek =", peek.hex())
# peek = 7dd4f19ad6b80c973209e59d862094348d855f4259a430a0b9008cf9b24ce9295206b6bd9ec4d2a4
