#!/bin/bash

for i in {1..20}; do
    file="fc$i"
    host="-- enter your ip/hostname here --"
    ssh $host "mkdir -p /path/to/folder"
    scp $file $host:/path/to/folder/
    if [ $? -eq 0 ]; then
        echo "File $file copied successfully."
        ssh $host "sudo systemctl restart service_name"
    else
        echo "Error copying file."
    fi
done
