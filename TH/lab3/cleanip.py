import csv

def remove_duplicates(input_file, output_file):
    # Sử dụng set để loại bỏ các IP trùng lặp
    unique_ips = set()

    # Đọc IP từ file input_file
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            ip = row[0].strip()  # Lấy IP và loại bỏ khoảng trắng
            if ip:  # Nếu IP không rỗng, thêm vào set
                unique_ips.add(ip)

    # Ghi các IP duy nhất vào file output_file
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for ip in unique_ips:
            writer.writerow([ip])

    print(f"Đã loại bỏ IP trùng lặp. Kết quả được lưu trong {output_file}.")

# Đường dẫn tới file đầu vào và đầu ra
input_file = 'ip_uit.csv'
output_file = 'unique_IP_uit.csv'

# Thực hiện loại bỏ IP trùng lặp
remove_duplicates(input_file, output_file)
