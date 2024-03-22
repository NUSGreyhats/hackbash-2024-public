#!/usr/bin/python3
import pty
from secrets import token_hex
import subprocess
import sys
import os
import signal

class Alarm(Exception):
    pass

def alarm_handler(signum, frame):
    raise Alarm

def main():

    username = token_hex(6)
    jail = f"/home/{username}"
    if os.path.exists(f"/home/{username}"):
        print("ERROR! please try to reconnect.")
        sys.exit(0)

    os.system(f"useradd -m {username} -s /bin/bash")
    os.system(f"rm {jail}/.bash* {jail}/.profile")
    os.system(f"chown root:root {jail}")
    os.system(f"chmod 755 {jail}")
    os.system(f"cp -rp /etc /bin /lib /lib64 /usr {jail}")
    os.system(f"mkdir -p {jail}/home/player")

    # place challenge files inside!
    os.system(f"cp -p /snek.txt {jail}/flag.txt")
    os.system(f"cp -p /.hello.py /hello {jail}/home/player/")
    os.system(f"cp -p /passwd {jail}/etc/passwd")
    os.system(f"cp -p /group {jail}/etc/group")
    os.system(f"cp -p /shadow {jail}/etc/shadow")
    os.system(f"chown 1000:1000 {jail}/home/player")

    # install timeout
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(60*10)  # 2 minutes

    try:
        os.chdir(jail)
        subprocess.run(["/usr/sbin/chroot", "./", f"./bin/su", "player"])
    except Alarm:
        print(f"TIMEOUT!");

    os.system(f"userdel {username}")
    os.system(f"rm -rf /home/{username}")

main()
