from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from random import randbytes

msg = open("email","rb").read()
key = randbytes(1)*16 # 16 byte key is very long hard to guess!!!
cipher = AES.new(key, AES.MODE_ECB)
enc = cipher.encrypt(pad(msg,16))
with open("enc","wb") as f:
    f.write(enc)
