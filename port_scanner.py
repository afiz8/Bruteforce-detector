# port_scanner.py
import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        sock.close()

# Contoh pemakaian
target_ip = input("Masukkan IP atau domain target: ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]
scan_ports(target_ip, common_ports)