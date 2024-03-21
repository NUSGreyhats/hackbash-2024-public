from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
from secrets import randbelow

def pad(msg:bytes):
    assert len(msg) < 128
    if len(msg) == 127:
        return b"\0" + msg
    padding_len = 128 - len(msg) - 2
    padding = bytes([randbelow(254) + 1 for _ in range(padding_len)])
    return b"\0" + padding + b"\0" + msg

def unpad(msg:bytes):
    assert msg[:1] == b"\0"
    if b"\0" in msg[1:]:
        return msg[2+msg[1:].index(b"\0"):]
    return msg[1:]

flag = b"flag{omg_pwease_dowt_do_twis_to_mwe_pwease}" # omitted
m = bytes_to_long(pad(flag))

p,q = getPrime(512), getPrime(512)
n = p*q
e = 0x10001
d = pow(e, -1, (p-1)*(q-1))
encrypted_flag = pow(m, e, n)
print("encrypted_flag =", encrypted_flag)
print("n =", n)

def decrypt(c):
    try:
        unpad(long_to_bytes(pow(c, d, n), 128))
        return True
    except:
        return False

while True:
    data = int(input("Input (int): "))
    output = decrypt(data)
    print("Output (bool): ", output, flush=True)