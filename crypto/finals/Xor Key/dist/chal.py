import string
from secrets import choice, os, randbelow
from itertools import cycle

flag = "flag{XXXXXXXXXXXXXXXXXXXXXXX}" # I've replaced the flag chars with `X`

allowed_chars = string.printable
plaintext = [choice(allowed_chars) for _ in range(10000)]
pos = randbelow(len(plaintext) - len(flag))
plaintext[pos:pos+len(flag)] = [*flag]
plaintext = "".join(plaintext).encode()

key = os.urandom(30)
ciphertext = bytes([x^y for x,y in zip(cycle(key), plaintext)])
open("enc", "wb").write(ciphertext)
