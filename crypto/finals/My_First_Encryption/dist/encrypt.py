import hashlib
from binascii import hexlify

def xor(a, b):
    res = bytes([i ^ j for i, j in zip(a,b)])
    return res

def main():
    flag = "flag{<REDACTED>}"
    hashy = [hashlib.sha1(i.encode()).digest() for i in flag]
    key = [hashy[i] for i in range(4)]
    for i in key:
        for j in range(len(hashy)):
            hashy[j] = xor(i, hashy[j])

    with open("cipher.txt", "wb") as f:
        for i in hashy:
            f.write(i)
            f.write("\r\n".encode())

main()
