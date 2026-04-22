# Port Scanner

A simple Python port scanner that checks for open ports on a target IP address. Useful for network troubleshooting, security auditing, and learning socket programming.

## Features
- Scans common ports (21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995, 3306, 3389, 5432, 8080)
- 1-second timeout per port
- Clear open/closed output with emojis
- No external dependencies (uses Python's built-in `socket`)

## How to Use
1. **Run the script**
   ```bash
   python scanner.py


2. **Enter an IP address when prompted (e.g., 8.8.8.8 or your own server IP)**

   Example Output

   ```text
   Enter IP address to scan: 8.230.114.131

   Scanning 8.230.114.131 for common open ports...

   ❌ Port 21 is closed
   ✅ Port 22 is OPEN
   ❌ Port 23 is closed
   ...
   ✅ Scan complete. Found 1 open port(s).
   Open ports: [22]
   
**What I Learned** 

   TCP/IP and how ports work

   Socket programming in Python

   Connection timeouts

   Basic security scanning concepts
