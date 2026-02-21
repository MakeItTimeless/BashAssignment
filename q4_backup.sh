#!/bin/bash

# Q4 Backup Script

echo "BACKUP SCRIPT"

read -p "Enter source directory: " source

if [ ! -d "$source" ]; then
    echo "Source directory not found!"
    exit 1
fi

read -p "Enter destination directory: " dest
mkdir -p "$dest"

echo "Choose Backup Type:"
echo "1. Simple Copy"
echo "2. Compressed (tar.gz)"
read -p "Choice: " choice

timestamp=$(date +%Y%m%d_%H%M%S)

start=$(date +%s)

if [ "$choice" -eq 1 ]; then
    cp -r "$source" "$dest/backup_$timestamp"
    backupfile="$dest/backup_$timestamp"
elif [ "$choice" -eq 2 ]; then
    tar -czf "$dest/backup_$timestamp.tar.gz" "$source"
    backupfile="$dest/backup_$timestamp.tar.gz"
else
    echo "Invalid option"
    exit 1
fi

end=$(date +%s)
duration=$((end-start))

if [ -e "$backupfile" ]; then
    echo
    echo "Backup completed successfully!"
    echo "File: $backupfile"
    du -sh "$backupfile"
    echo "Time taken: $duration seconds"
else
    echo "Backup failed!"
fi
