import socket
import requests
import subprocess

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except:
        return "Could not fetch (check internet)"

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_dns_servers():
    try:
        # Windows command to show DNS servers
        result = subprocess.run(['ipconfig', '/all'], capture_output=True, text=True)
        lines = result.stdout.split('\n')
        dns = []
        for line in lines:
            if 'DNS Servers' in line:
                parts = line.split(':')
                if len(parts) > 1:
                    dns.append(parts[1].strip())
        return dns if dns else ["Not found"]
    except:
        return ["Could not retrieve"]

def main():
    print("=== Network Information ===\n")
    print(f"Public IP: {get_public_ip()}")
    print(f"Local IP: {get_local_ip()}")
    print(f"Hostname: {socket.gethostname()}")
    print(f"DNS Servers: {', '.join(get_dns_servers())}")

if __name__ == "__main__":
    main()