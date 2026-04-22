import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def main():
    target = input("Enter IP address to scan: ")
    print(f"\nScanning {target} for common open ports...\n")
    
    common_ports = [21,22,23,25,53,80,110,143,443,993,995,3306,3389,5432,8080]
    open_ports = []
    
    for port in common_ports:
        if scan_port(target, port):
            print(f"✅ Port {port} is OPEN")
            open_ports.append(port)
        else:
            print(f"❌ Port {port} is closed")
    
    print(f"\n✅ Scan complete. Found {len(open_ports)} open port(s).")
    if open_ports:
        print(f"Open ports: {open_ports}")

if __name__ == "__main__":
    main()
