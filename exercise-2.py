def count_and_sort_ips(file_path):
    ip_addresses = []
    
    # Read the file and extract IP addresses
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            ip_addresses.append(line)
    
    # Print the total number of IP addresses
    print(f"Total IP addresses: {len(ip_addresses)}")
    
    # Sort and print the IP addresses in ascending order
    sorted_ips = sorted(ip_addresses)
    for ip in sorted_ips:
        print(ip)


# Test the function with a sample file
file_path = "ip_addresses.txt"  # Replace with the path to your file
count_and_sort_ips(file_path)
