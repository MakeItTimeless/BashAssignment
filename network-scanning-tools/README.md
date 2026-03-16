# Network Scanning Automation

## Project Overview
This project automates common network reconnaissance tasks using Python.

Three network scanning tools are implemented:

1. Ping Scanner
2. ARP Scanner
3. Nmap Scanner

These tools execute system networking commands and parse their outputs using Python.

---

## Tools Used

- Python 3
- Nmap
- Linux networking tools (Ping, ARP)
- Python modules:
  - subprocess
  - platform
  - re
  - sys

---

## Installation

### Install Python

Check Python version:

python3 --version

Python 3.6 or higher is required.

---

### Install Nmap

Linux:

sudo apt install nmap

Mac:

brew install nmap

Windows:

Download from https://nmap.org/download.html

---
```
## Project Structure
network-scanning-tools/
│
├── ping_scanner.py
├── arp_scanner.py
├── nmap_scanner.py
├── README.md
│
└── screenshots/
├── ping_output.png
├── arp_output.png
└── nmap_output.png

```

---

## How to Run Programs

### Ping Scanner

Run:

python3 ping_scanner.py

Example:

Ping single host? (y/n): y  
Enter hostname or IP: google.com

---

### ARP Scanner

Run:

python3 arp_scanner.py

This displays IP and MAC address mappings from the ARP table.

---

### Nmap Scanner

Run:

python3 nmap_scanner.py

Select scan type:

1 - Host discovery 
2 - Port scan 
3 - Service version detection

---

## Example Output

Ping Scanner

Host: google.com 
Status: Reachable 
Average Time: 23 ms

---

ARP Scanner

IP Address        MAC Address 
172.17.144.1      00:15:5d:68:d3:73 

Total entries: 1

---

Nmap Scanner

PORT    STATE SERVICE 
22/tcp  open  ssh 
80/tcp  open  http 

---

## Author

Srijani 
Cybersecurity Assignment 
Network Scanning Automation
