"""
Ping Scanner
------------

This program automates the ping command using Python.
It checks whether a host is reachable and extracts
the average response time.

Features:
- Single host scanning
- Multiple host scanning
- Cross-platform compatibility
- Error handling

Author: Srijani
Course: Cybersecurity
Assignment: Network Scanning Automation
"""

import subprocess
import platform
import re
import sys

# ---------------------------------------------
# Utility Functions
# These functions handle ping execution,
# OS detection, and response parsing.
# ---------------------------------------------

def get_ping_parameter():
    """
    Returns the correct ping parameter depending on OS.

    Windows uses '-n'
    Linux/Mac uses '-c'
    """

    os_type = platform.system().lower()

    if os_type == "windows":
        return "-n"
    else:
        return "-c"


def ping_host(host):
    """
    Pings a given host and checks if it is reachable.

    Parameters:
        host (str): Hostname or IP address

    Returns:
        dict: host status and average response time
    """

    param = get_ping_parameter()

    command = ["ping", param, "4", host]

    try:
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10
        )

        output = result.stdout

        if result.returncode == 0:
            status = "Reachable"
        else:
            status = "Unreachable"

        avg_time = extract_average_time(output)

        return {
            "host": host,
            "status": status,
            "avg_time": avg_time
        }

    except subprocess.TimeoutExpired:
        return {
            "host": host,
            "status": "Timeout",
            "avg_time": "N/A"
        }

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


def extract_average_time(ping_output):
    """
    Extracts the average response time from the ping output.

    Parameters:
        ping_output (str): Raw output from the ping command

    Returns:
        str: Average response time in milliseconds
    """

    # Regex pattern to find average time
    pattern = r"= .*?/.*?/([0-9.]+)/|Average = (\d+)ms"

    match = re.search(pattern, ping_output)

    if match:
        if match.group(1):
            return match.group(1) + " ms"
        elif match.group(2):
            return match.group(2) + " ms"

    return "N/A"


if __name__ == "__main__":
    """
    Main execution block of the program.
    Handles user input and displays results.
    """

    print("=== Ping Scanner ===")

    choice = input("Ping single host? (y/n): ").lower()

    if choice == "y":
        host = input("Enter hostname or IP: ")

        result = ping_host(host)

        print("\nHost:", result["host"])
        print("Status:", result["status"])
        print("Average Time:", result["avg_time"])

    else:
        hosts_input = input("Enter multiple hosts separated by space: ")

        hosts = hosts_input.split()

        for host in hosts:
            result = ping_host(host)

            print("\nHost:", result["host"])
            print("Status:", result["status"])
            print("Average Time:", result["avg_time"])
