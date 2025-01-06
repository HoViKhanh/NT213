#!/bin/bash

# Định nghĩa file đầu vào và file đầu ra
input_file="port_uit.txt"
output_file="result_port_uit.csv"

# Xóa file kết quả nếu đã tồn tại
> "$output_file"

# Thêm dòng tiêu đề vào file CSV
echo "IP,Port" >> "$output_file"

# Biến để lưu IP hiện tại
current_ip=""

# Đọc từng dòng trong file đầu vào
while IFS= read -r line; do
    # Kiểm tra dòng chứa thông tin IP
    if [[ $line =~ Nmap\ scan\ report\ for\ ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+) ]]; then
        current_ip="${BASH_REMATCH[1]}"
    # Kiểm tra các dòng chứa thông tin port mở
    elif [[ $line =~ ([0-9]+)\/tcp\ *open ]]; then
        port="${BASH_REMATCH[1]}"
        # Ghi IP và port vào file CSV
        echo "$current_ip,$port" >> "$output_file"
    fi
done < "$input_file"

echo "Kết quả đã được lưu vào file $output_file"
