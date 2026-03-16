"""
Nmap Scanner
------------

This program automates Nmap network scanning using Python.

Features:
- Checks if Nmap is installed
- Performs different types of scans
- Displays scan results
- Handles errors gracefully

Author: Srijani
Course: Cybersecurity
Assignment: Network Scanning Automation
"""


import subprocess
import sys


def check_nmap_installed():
    """
    Checks if Nmap is installed on the system.
    """

    try:
        result = subprocess.run(
            ["nmap", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print("Nmap is installed.\n")
        else:
            print("Nmap is not installed.")
            sys.exit(1)

    except FileNotFoundError:
        print("Nmap is not installed. Please install Nmap first.")
        sys.exit(1)


def run_nmap_scan(target, scan_type):
    """
    Runs the selected Nmap scan on the target.

    Parameters:
        target (str): Target IP address or hostname
        scan_type (str): Type of scan selected
    """

    if scan_type == "1":
        command = ["nmap", "-sn", target]   # Host discovery

    elif scan_type == "2":
        command = ["nmap", target]         # Default port scan

    elif scan_type == "3":
        command = ["nmap", "-sV", target]  # Service version detection

    else:
        print("Invalid scan type.")
        return

    try:
        print("\nScanning... Please wait\n")

        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("Scan completed successfully.\n")
        print("Results:")
        print("========================================")

        print(result.stdout)

        print("========================================")

    except Exception as e:
        print("Error running Nmap scan:", e)
        sys.exit(1)


if __name__ == "__main__":
    """
    Main execution block for Nmap scanner
    """

    print("=== Nmap Scanner ===\n")

    # Check if Nmap is installed
    check_nmap_installed()

    # Get target input
    target = input("Enter target IP or hostname: ")

    print("\nSelect scan type:")
    print("1. Basic Host Discovery (-sn)")
    print("2. Port Scan (default)")
    print("3. Service Version Detection (-sV)")

    choice = input("\nEnter choice (1-3): ")

    # Run the scan
    run_nmap_scan(target, choice)
