import socket
import csv
def resolve_ips(domain):
    try:

        _, _, ip_addresses = socket.gethostbyname_ex(domain)
        return ip_addresses
    except socket.gaierror:
        return None
def main():
    input_file = 'BT1.csv'
    output_file1 = 'resolved_ips.csv'
    

    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        
        with open(output_file1, mode='w', newline='') as output1:
            
            writer1 = csv.writer(output1)
            writer1.writerow(['Domain', 'IP Addresses'])

            for row in reader:
                domain = row[0].strip()
                ips = resolve_ips(domain)
                if ips:
                    ip_list = ', '.join(ips)  
                    print(f"{domain} : {ip_list}")
                    writer1.writerow([domain, ip_list])
                else:
                    print(f"{domain} : Không tìm thấy IP")
                    writer1.writerow([domain, 'Không tìm thấy IP'])

if __name__ == '__main__':
    main()
