import nmap

scanner = nmap.PortScanner()
target_ip = "scanme.nmap.org"  # Change this to your IP

print(f"🔍 Scanning target: {target_ip}...")

try:
    scanner.scan(target_ip, "22-80")  # Scanning ports 22 to 80
    for host in scanner.all_hosts():
        print(f"✅ Host found: {host} ({scanner[host].hostname()})")
        for proto in scanner[host].all_protocols():
            print(f"📡 Protocol: {proto}")
            for port in scanner[host][proto].keys():
                print(f"🟢 Port {port} is {scanner[host][proto][port]['state']}")
except Exception as e:
    print(f"❌ Error running scan: {e}")

