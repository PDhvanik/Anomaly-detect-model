from scapy.all import IP, TCP, UDP, send, sniff, Ether, ARP
import pandas as pd
import random
import time
import socket

RESULT_FILE = "labeled_anomaly_dataset.csv"
packets_list = []


def create_packet_record(pkt, label):
    time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    src = dst = proto = src_port = dst_port = 0

    if pkt.haslayer(IP):
        ip = pkt[IP]
        src, dst = ip.src, ip.dst
        proto = 'TCP' if pkt.haslayer(
            TCP) else 'UDP' if pkt.haslayer(UDP) else 'IP'
        if pkt.haslayer(TCP):
            src_port = pkt[TCP].sport
            dst_port = pkt[TCP].dport
        elif pkt.haslayer(UDP):
            src_port = pkt[UDP].sport
            dst_port = pkt[UDP].dport
    elif pkt.haslayer(ARP):
        src = pkt[ARP].psrc
        dst = pkt[ARP].pdst
        proto = 'ARP'

    packets_list.append({
        "Time": time_str,
        "Source": src,
        "Destination": dst,
        "Protocol": proto,
        "Length": len(pkt),
        "Source Port": src_port,
        "Destination Port": dst_port,
        "bad_packet": label
    })


# 1. Simulate Normal Traffic
print("[*] Generating normal traffic...")
for i in range(10000):
    pkt = IP(src="192.168.1.10", dst="192.168.1.1") / \
        TCP(sport=12345, dport=80)
    create_packet_record(pkt, 0)
    time.sleep(0.01)

# 2. Simulate TCP Anomalous Traffic
print("[*] Generating anomalous TCP packets...")
for i in range(1000):
    pkt = IP(src="192.167.5.200", dst="192.167.5.35") / \
        TCP(sport=random.randint(50000, 60000), dport=random.randint(50000, 60000)) / \
        ("X" * random.randint(5, 1000))
    create_packet_record(pkt, 1)
    time.sleep(0.005)

# 3. Simulate UDP Flood Attack
print("[*] Generating UDP flood packets...")
for i in range(1000):
    src_ip = f"192.168.29.{random.randint(10, 100)}"
    pkt = IP(src=src_ip, dst="192.168.29.13") / UDP(sport=random.randint(1024, 65535), dport=8080) / \
        bytes(random.randint(20, 100))
    create_packet_record(pkt, 1)
    time.sleep(0.005)

# Save all packets to CSV
df = pd.DataFrame(packets_list)
df.to_csv(RESULT_FILE, index=False)
print(f"[+] Labeled dataset saved to {RESULT_FILE}")
