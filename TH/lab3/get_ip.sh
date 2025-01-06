#!/bin/bash
while IFS= read -r domain; do
    ip=$(nslookup "$domain" | grep -Eo 'Address: ([0-9]{1,3}\.){3}[0-9]{1,3}' | awk '{print $2}' | head -n 1)
    if [ -n "$ip" ]; then
        echo "$ip" >> ip_uit.txt
    else
        echo "Không thể lấy IP cho domain: $domain"
    fi
done < domain_uit.txt

