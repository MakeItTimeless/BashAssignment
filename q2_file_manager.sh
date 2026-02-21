#!/bin/bash

# Q2 File Manager Script

while true
do
    echo "===== FILE MANAGER ====="
    echo "1. List files"
    echo "2. Create directory"
    echo "3. Create file"
    echo "4. Delete file"
    echo "5. Rename file"
    echo "6. Search file"
    echo "7. Count files and directories"
    echo "8. Exit"
    echo "========================="

    read -p "Enter choice: " choice

    case $choice in
1)
ls -lh
;;
2)
read -p "Enter directory name: " dirname
mkdir "$dirname"
echo "Directory created"
;;
3)
read -p "Enter file name: " filename
touch "$filename"
echo "File created"
;;
4)
read -p "Enter file name to delete: " filedel
if [ -f "$filedel" ]; then
    rm "$filedel"
    echo "File deleted"
else
    echo "File not found"
fi
;;
5)
read -p "Old name: " old
read -p "New name: " new
mv "$old" "$new"
echo "Renamed successfully"
;;
6)
read -p "Enter file name to search: " search
find . -name "$search"
;;
7)
echo "Files:"
ls -l | grep ^- | wc -l
echo "Directories:"
ls -l | grep ^d | wc -l
;;
8)
echo "Exiting..."
exit
;;
*)
echo "Invalid option"
;;
esac
done
