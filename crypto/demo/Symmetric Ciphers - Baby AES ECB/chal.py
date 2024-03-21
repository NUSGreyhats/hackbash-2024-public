from Crypto.Cipher import AES
from random import randbytes
from Crypto.Util.Padding import pad

cipher = AES.new(randbytes(16),AES.MODE_ECB)
email = open("email","rb").read()

with open("enc","wb") as f:
    for i in email:
        f.write(cipher.encrypt(pad(bytes([i]),16)))
