import scapy.all as scapy 

# This file is NOT to be given to participants
# To solve, run filter `icmp && ip.src == 192.168.121.1` in Wireshark on `challenge.cap` and save filtered packets as `challenge2.pcap`. Then, run `solve.py`

scapy_cap = scapy.rdpcap('challenge2.pcapng')
with open('output', 'wb') as f:
    for packet in scapy_cap:
        data = bytes(packet.payload)[-8:]
        print(data.decode(),end="")