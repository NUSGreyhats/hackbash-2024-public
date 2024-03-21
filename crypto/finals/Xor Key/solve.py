ciphertext = open("dist/enc", "rb").read()

import string
from functools import reduce
from itertools import cycle
import re

allowed_chars = set((string.printable).encode())
klen = 30

keydict = {ct:set([c^ct for c in allowed_chars]) for ct in range(0x100)}
keypos = [reduce(lambda x,y: x&y, (keydict[c] for c in ciphertext[kidx::klen])) for kidx in range(klen)]
assert all(len(x)==1 for x in keypos)
key = [next(iter(k)) for k in keypos]

plaintext = bytes([x^y for x,y in zip(cycle(key), ciphertext)]).decode()
flag = re.findall(r"flag{[^}]+}", plaintext)[0]
print(flag)