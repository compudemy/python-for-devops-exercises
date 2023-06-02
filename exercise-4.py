from collections import defaultdict

def count_unique_ips(log_file):
    ip_counts = defaultdict(int)
    
    # Read the log file and count IP occurrences
    with open(log_file, 'r') as file:
        for line in file:
            line = line.strip()
            ip = line.split()[0]  # Assuming the IP address is the first token in each line
            ip_counts[ip] += 1
    
    # Print the IP addresses and their counts in descending order
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
    for ip, count in sorted_ips:
        print(f"IP: {ip}, Count: {count}")


# Test the function with a sample log file
log_file_path = "access.log"  # Replace with the path to your log file
count_unique_ips(log_file_path)
