from nclib import Netcat
from functools import reduce
from Crypto.Util.number import long_to_bytes, bytes_to_long

nc = Netcat(("127.0.0.1", 55001))
nqueries = 0
def encrypt_data(data:str) -> str:
    global nqueries; nqueries += 1
    nc.recv_until(b": ")
    nc.sendline(data.encode())
    nc.recv_until(b": ")
    ct = nc.recv_line().decode().strip()
    return ct

allowed_chars = b'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '
str1 = b"data="
str2 = b",flag="
xor = lambda *x: reduce(lambda a,b: bytes(x^y for x,y in zip(a,b)), x)

rec_flag = b""
while b"}" not in rec_flag:
    
    data = b"".join([
        b"A"*(16 - len(str1)),
        b"A"*(160-len(str2)-len(rec_flag)-1)
    ])
    ct = encrypt_data(data.hex())
    biv = bytes_to_long(bytes.fromhex(ct[:32]))
    blk = ct[352:384]
    
    for i,g in enumerate(allowed_chars):
        g = bytes([g])
        bivdiff = xor(long_to_bytes(biv), long_to_bytes(biv + i + 1))[-16 + len(str1):]
        data = b"".join([
            xor(b"A"*(16 - len(str1)), bivdiff),
            b"A"*(160-len(str2)-len(rec_flag)-1),
            str2 + rec_flag + g
        ])
        ct = encrypt_data(data.hex())
        if blk == ct[352:384]:
            break
    else: raise Exception()
    rec_flag += g
    print(rec_flag.decode())

print("\n\n========= FINAL FLAG =========")
print(rec_flag.decode())
print("========= FINAL FLAG =========")
print("Number of queries:", nqueries)