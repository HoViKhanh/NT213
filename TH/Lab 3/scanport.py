import socket
import csv

# Hàm kiểm tra xem một cổng có mở trên địa chỉ IP hay không
def is_port_open(ip, port):
    try:
        # Tạo socket và kết nối với địa chỉ IP và cổng
        with socket.create_connection((ip, port), timeout=1):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

# Đọc danh sách IP từ file IP.csv
def read_ip_list(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

# Đọc danh sách cổng từ file port.csv
def read_port_list(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return [row[0] for row in reader]

# Quét các cổng trên danh sách IP và lưu kết quả vào file result_port.csv
def scan_ports(ip_list, port_list, result_file):
    with open(result_file, 'w', newline='') as file:
        writer = csv.writer(file)
        # Ghi tiêu đề cột
        writer.writerow(['IP Address', 'Port', 'Status'])
        # Duyệt qua từng IP và cổng, kiểm tra trạng thái cổng
        for ip in ip_list:
            for port in port_list:
                if is_port_open(ip, port):
                    # Ghi kết quả vào file CSV nếu cổng mở
                    writer.writerow([ip, port, 'Open'])
                    print(f"{ip}:{port} is Open")

# Đường dẫn tới các file
ip_file = 'unique_IP.csv'
port_file = 'port_vertical.csv'
result_file = 'result_port.csv'

# Đọc danh sách IP và cổng
ip_list = read_ip_list(ip_file)
port_list = read_port_list(port_file)

# Thực hiện quét và lưu kết quả
scan_ports(ip_list, port_list, result_file)
