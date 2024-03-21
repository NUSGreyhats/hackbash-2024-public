#!/bin/python3
import subprocess

print("Hello")
print("here's a flag\n")

subprocess.run(["bash", "-c", "echo ' ------------------------' > /helloflag.txt"])
subprocess.run(["bash", "-c", "echo '| imagine not being able |' >> /helloflag.txt"])
subprocess.run(["bash", "-c", "echo '| to read /flag.txt      |' >> /helloflag.txt"])
subprocess.run(["bash", "-c", "echo '|------------------------ ' >> /helloflag.txt"])
subprocess.run(["bash", "-c", "echo '|' >> /helloflag.txt"])
subprocess.run(["bash", "-c", "echo '|' >> /helloflag.txt"])
subprocess.run(["bash", "-c", "cat /helloflag.txt"])
