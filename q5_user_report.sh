#!/bin/bash

# Q5 User Report Script

echo " USER ACCOUNT REPORT "
echo

# Total users
total=$(wc -l < /etc/passwd)
echo "Total Users: $total"

# System users (UID < 1000)
sys=$(awk -F: '$3 < 1000 {count++} END {print count}' /etc/passwd)
echo "System Users: $sys"

# Normal users (UID >=1000)
normal=$(awk -F: '$3 >= 1000 {count++} END {print count}' /etc/passwd)
echo "Normal Users: $normal"

echo
echo "Currently Logged-in Users:"
who
echo

# UID 0 users
echo "Users with UID 0 (Admin level):"
awk -F: '$3==0 {print $1}' /etc/passwd
echo

# Users without password
echo "Users without passwords:"
awk -F: '($2==""){print $1}' /etc/shadow 2>/dev/null
echo

# Inactive users (never logged in)
echo "Inactive Users:"
lastlog | grep "**Never logged in**"
echo

# Table header
echo "----- USER DETAILS TABLE -----"
printf "%-15s %-10s %-20s %-15s\n" "USERNAME" "UID" "HOME" "SHELL"

awk -F: '{printf "%-15s %-10s %-20s %-15s\n",$1,$3,$6,$7}' /etc/passwd
