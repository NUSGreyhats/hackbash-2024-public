# Challenge Summary

SUID misuse challenge. `lore.txt` hints at a misconfigured SUID binary existing somewhere within the file system.

`find / -perm -u=s -type f 2>/dev/null` allows us to find all suid files in the file system.

`/usr/bin/time` is a SUID file, which is odd. If you look in GTFObins, you see `/usr/bin/time /bin/bash -p` gives you a root shell, allowing you to read the flag file. 

`-p` flag specifies to not drop privileges.

# Details

don't forget to read the lore

the flag is in /flag.txt

# Author

Jin Kai

# Hints

nil

# Flag

`flag{even_time_could_tell_a_shell??}`

# Learning Objectives

suid binary misconfiguration

privilege escalation
