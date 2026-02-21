#!/bin/bash

# Q1 Script — Displays system information

current_user=$(whoami)
machine=$(hostname)
current_time=$(date)
system=$(uname -s)
current_dir=$(pwd)
home_dir=$HOME
logged_users=$(who | wc -l)
system_uptime=$(uptime -p)

echo "========== SYSTEM DETAILS =========="
echo "User Name      : $current_user"
echo "Host Name      : $machine"
echo "Date & Time    : $current_time"
echo "Operating Sys  : $system"
echo "Working Dir    : $current_dir"
echo "Home Dir       : $home_dir"
echo "Users Online   : $logged_users"
echo "Uptime         : $system_uptime"
echo "===================================="
