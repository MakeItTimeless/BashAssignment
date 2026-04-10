import socket
import time

target = input("Enter target IP: ")
ports = input("Enter ports (comma separated): ")

port_list = [int(p.strip()) for p in ports.split(",")]

start_time = time.time()

print(f"\nStarting scan on {target}...\n")

file = open("scan_results.txt", "w")

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port}: OPEN")
        file.write(f"Port {port}: OPEN\n")
    else:
        print(f"Port {port}: CLOSED")
        file.write(f"Port {port}: CLOSED\n")

    s.close()

end_time = time.time()

duration = end_time - start_time

print(f"\nScan completed in {duration:.2f} seconds")
file.write(f"\nScan Time: {duration:.2f} seconds")

file.close()
