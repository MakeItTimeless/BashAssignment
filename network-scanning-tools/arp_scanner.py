"""
ARP Scanner
-----------

This program retrieves the system ARP table
and extracts IP-MAC address mappings.

Features:
- Retrieves ARP table
- Parses IP and MAC addresses
- Displays results in formatted table
- Counts total ARP entries

Author: Srijani
Course: Cybersecurity
Assignment: Network Scanning Automation
"""

import subprocess
import platform
import re
import sys


def get_arp_table():
    """
    Retrieves the ARP table from the system.

    Returns:
        str: Raw ARP table output
    """

    try:
        command = ["arp", "-a"]

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout

    except Exception as e:
        print("Error retrieving ARP table:", e)
        sys.exit(1)


def parse_arp_table(arp_output):
    """
    Parses ARP table output and extracts IP-MAC mappings.

    Parameters:
        arp_output (str): Raw ARP table output

    Returns:
        list: List of tuples containing (IP, MAC)
    """

    entries = []

    # Regex pattern for IP and MAC address
    pattern = r"\((\d+\.\d+\.\d+\.\d+)\) at ([0-9a-f:]{17})"

    matches = re.findall(pattern, arp_output)

    for match in matches:
        ip = match[0]
        mac = match[1]
        entries.append((ip, mac))

    return entries


def display_results(entries):
    """
    Displays the ARP entries in a formatted table.

    Parameters:
        entries (list): List of (IP, MAC) tuples
    """

    print("\nIP Address           MAC Address")
    print("----------------------------------------")

    for ip, mac in entries:
        print(f"{ip:<20} {mac}")

    print("\nTotal entries:", len(entries))


if __name__ == "__main__":
    """
    Main execution block for ARP scanner
    """

    print("=== ARP Scanner ===")
    print("Scanning ARP table...\n")

    # Get raw ARP table
    arp_output = get_arp_table()

    # Parse IP and MAC addresses
    entries = parse_arp_table(arp_output)

    # Display results
    display_results(entries)
