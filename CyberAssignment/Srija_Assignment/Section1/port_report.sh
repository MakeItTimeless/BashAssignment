#!/bin/bash

# Check if IP is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <target_ip>"
    exit 1
fi

TARGET=$1
DATE=$(date +%Y-%m-%d)
OUTPUT="scan_${TARGET}_${DATE}.txt"

echo "Scanning target: $TARGET"
echo "Results will be saved in $OUTPUT"

# Ports to scan
ports=(21 22 80 443 3306)

open_count=0

echo "Scan Report for $TARGET" > $OUTPUT
echo "Date: $DATE" >> $OUTPUT
echo "------------------------" >> $OUTPUT

for port in "${ports[@]}"
do
    timeout 1 bash -c "echo >/dev/tcp/$TARGET/$port" 2>/dev/null

    if [ $? -eq 0 ]; then
        echo "Port $port: OPEN" | tee -a $OUTPUT
        open_count=$((open_count+1))
    else
        echo "Port $port: CLOSED" >> $OUTPUT
    fi
done

echo "------------------------" >> $OUTPUT
echo "Total Open Ports: $open_count" | tee -a $OUTPUT
