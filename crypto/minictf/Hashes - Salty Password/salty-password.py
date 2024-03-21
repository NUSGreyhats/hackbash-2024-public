import hashlib

saltList = ["ketchup", "pepper", "garlic", "truffle", "black pepper"]
passwordList = ["ilovejames", "hackbash420", "p@ssW0rd", "3eefferferfef", "qwertyuiopoiuytrewq"]
hashList = ["b121216e8b4db2fbf98266c34128a8d77b0ba804f46ab634ada38cf05ac44a42",
        "3fb52e34f89eff659d2b1efc4a8073039404668602257497e0cb0783e85310c1",
        "6e4258d0250267c6354cd29a3cf1bb9784a7ad7824dff9c576a3b6c422255fac",
        "ce708f6c7ddb2b77e984343404adb33d1c9455551d04ea4cc75566bc53962d4f",
        "244066b39fc9fdad6af785341664e7bc504a87b6dc2de6770d91afd28a0ae6a6"]

#Strings are encoded in UTF-8 and hashed with SHA-256
#Find the correct sequence of digits
#If the first salt and third password is the first hash, then your first two digits are 13
#If the third salt and fourth password is the 3rd hash, then your 5th and 6th digits are 34
#Flag will be flag{ //with your sequence of digits here// }
#Sample flag{1234123411}

#change the flag to be the correct sequence
flag = "flag{1234123411}"

#Function to help check if your flag is correct
def check(flag):
        count = 0
        digitSequence = str(flag[5:15])
        print("Digital Sequence:" + digitSequence)

        salt = 0
        password = 1
        hashIndex = 0

        for x in range(5):
                saltIndex = int(digitSequence[salt])
                print("Salt Index:" + str(saltIndex))
                passwordIndex = int(digitSequence[password])
                print("Password Index:" + str(passwordIndex))
                salted = saltList[saltIndex] + passwordList[passwordIndex]
                hashInput = hashlib.sha256(salted.encode('UTF-8'))

                salt += 2
                password += 2

                if hashList[hashIndex] == hashInput.hexdigest():
                        count += 1
                        hashIndex += 1
                else:
                        print("Invalid flag")
                        break

        if count == 5:
                print("Correct flag obtained!")

check(flag)