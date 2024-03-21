from pwn import *

# uncomment this line to connect to remote
# p = remote("chall.nusgreyhats.org", 61636)
p = process("./challenge")

p.sendline(b"payload goes here!")

p.interactive()
