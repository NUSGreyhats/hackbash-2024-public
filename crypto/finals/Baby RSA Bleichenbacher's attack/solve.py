from Crypto.Util.number import long_to_bytes
from nclib import Netcat

nc = Netcat(("127.0.0.1", 55002))
e = 0x10001
encrypted_flag = int(nc.recvline().split(b" = ")[1].strip().decode())
n = int(nc.recvline().split(b" = ")[1].strip().decode())

def unpad(msg:bytes):
    assert msg[:1] == b"\0"
    if b"\0" in msg[1:]:
        return msg[2+msg[1:].index(b"\0"):]
    return msg[1:]

nqueries = 0
def decrypt(data:int) -> int:
    global nqueries; nqueries += 1
    print(f"nqueries = {nqueries}   \r", end="")
    nc.recv_until(b": ")
    nc.sendline(str(data).encode())
    nc.recv_until(b": ")
    ct = nc.recv_line().decode().strip() == "True"
    return ct

def is_error(k):
    return not decrypt((pow(k,e,n) * encrypted_flag) % n)

t = n//(1<<(1024-8))
while not is_error(t+1): t += 1
while is_error(t+1): t += 1
for i in range(1024):
    upper = (n << i) // t
    lower = (n << i) // (t+1) + 1
    if upper==lower: break
    t = 2*t + is_error(2*t+1)
    
print("Flag =", unpad(long_to_bytes(lower, 128)).decode())
print("Queries =", nqueries)