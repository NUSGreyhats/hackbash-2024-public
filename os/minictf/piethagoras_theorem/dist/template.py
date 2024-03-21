from pwn import *

p = process("./challenge")

payload = b"payload goes here"
p.sendline(payload)

p.interactive()
