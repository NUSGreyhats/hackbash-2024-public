#!/usr/bin/python3
import subprocess
import sys

p = subprocess.Popen(["./challenge"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

p_out = p.communicate(input=input().encode())[0].decode()

if p.returncode < 0:
    print("Program crashed. Please try again!")
    sys.exit(0)
else:
    print(p_out)

if "You win!" in p_out:
    print("Wow, you did the impossible! You deserve this.")
    with open("./flag.txt", "r") as f:
        print(f.read())


