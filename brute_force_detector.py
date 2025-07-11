# brute_force_detector.py
failed_attempts = {
    '192.168.0.1': 5,
    '192.168.0.2': 12,
    '192.168.0.3': 2
}

threshold = 10

for ip, attempts in failed_attempts.items():
    if attempts > threshold:
        print(f"ALERT: IP {ip} might be performing a brute-force attack!")
    else:
        print(f"IP {ip} is safe.")