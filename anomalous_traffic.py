from scapy.all import IP, TCP, send
import random
import time

for i in range(50):
    pkt = IP(src="192.167.5.200", dst="192.167.5.35") / \
        TCP(sport=random.randint(50000, 60000), dport=random.randint(50000, 60000)) / \
        ("X" * random.randint(5, 1000))
    send(pkt, verbose=False)
    time.sleep(0.1)
