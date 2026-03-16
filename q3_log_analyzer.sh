#!/bin/bash

# Q3 Log Analyzer Script

if [ $# -eq 0 ]; then
    echo "Usage: $0 <logfile>"
    exit 1
fi

file=$1

if [ ! -f "$file" ]; then
    echo "Error: File does not exist"
    exit 1
fi

echo "===== LOG ANALYSIS ====="
echo "File: $file"
echo

# Total entries
total=$(wc -l < "$file")
echo "Total Entries: $total"
echo

# Unique IPs
echo "Unique IP Addresses:"
awk '{print $1}' "$file" | sort | uniq
echo

# Status codes
echo "Status Code Summary:"
awk '{print $NF}' "$file" | sort | uniq -c
echo

# Most accessed page
echo "Most Accessed Page:"
awk '{print $7}' "$file" | sort | uniq -c | sort -nr | head -1
echo

# Top 3 IPs
echo "Top 3 IP Addresses:"
awk '{print $1}' "$file" | sort | uniq -c | sort -nr | head -3
