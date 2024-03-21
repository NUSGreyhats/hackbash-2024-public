
xor = lambda a,b:bytes(i^j for i,j in zip(a,b))
f = [bytes.fromhex(i) for i in open("output","r").read().strip().split("\n")]

pad = [0x10]*0x10
orig = f[0]
f = f[16::16]
pt = xor(xor(orig,f[0])[-32:-16],pad)
pt = xor(xor(orig,f[1])[-32:-16],pad)+pt
pt = xor(xor(orig,f[2])[-32:-16],pad)+pt
pt = xor(xor(orig,f[3])[-32:-16],pad)+pt
print(pt)
