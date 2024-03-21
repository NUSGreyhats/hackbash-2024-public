# Challenge Summary
ICMP Data Exfiltration. Participants given `challenge.pcap` file only. To solve, run filter `icmp && ip.src == 192.168.121.1` in Wireshark on `challenge.cap` and save filtered packets as `challenge2.pcap`. Then, run `solve.py`

# Challenge Description
Someone has infiltrated into the Headquarters of Greyhats and retrieved classified information about HackBash. Luckily, we set up network traffic logging and captured all incoming and outgoing packets. We need your help to inspect the captured pcap file and find out what the intruder managed to find out about HackBash?  

# Author
Glendoodle

# Hints
If solving this challenge with python, the scapy python library might be useful. Install scapy by running 'pip install scapy' (Use 'sudo apt-get install python-scapy' if you still get an error after running 'pip install scapy'). Afterwards, you may work with the library by running something like this:

```
import scapy.all as scapy 

scapy_cap = scapy.rdpcap('challenge.pcapng')
with open('output', 'wb') as f:
    <do something>
```

# Flag
flag{ICMP_Exf1ltrat10n_C4n_B3_D3t3ct3d_By_Rul3Z}

# Learning Objectives
ICMP Data exfiltration and some scripting to extract relevant information from pcap file