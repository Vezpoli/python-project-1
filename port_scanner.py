import nmap

# Create a scanner object
scanner = nmap.PortScanner()

# Scan a target for open ports (adjust IP)
scanner.scan('192.168.1.1', '22-80')  # Scans ports 22 to 80

# Process results
for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
    print(f"State: {scanner[host].state()}")
    
    for proto in scanner[host].all_protocols():
        print(f"Protocol: {proto}")
        ports = scanner[host][proto].keys()
        for port in ports:
            print(f"Port {port}: {scanner[host][proto][port]['state']}")
