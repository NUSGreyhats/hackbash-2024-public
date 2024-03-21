import hashlib

def xor(a, b):
    res = bytes([i ^ j for i, j in zip(a,b)])
    return res

def main():
    known_flag = "flag"
    key = [hashlib.sha1(i.encode()).digest() for i in known_flag]
    with open("cipher.txt", "rb") as f:
        cipher = f.read().split("\r\n".encode())
        for i in key:
            for j in range(len(cipher)):
                cipher[j] = xor(i, cipher[j])

    with open("plain.txt", "w") as f:
        for i in cipher:
            f.write(i.hex())
            f.write("\n")
        
# place the remaining hash into crackstation
main()

