# NISHAD🚀 Basic TCP Port Scanner
A simple, fast, and foundational Python script for network reconnaissance and security auditing, designed to identify open TCP ports on a target host.

🎯 Project Objectives
This tool was developed to address common security and network visibility challenges:

Network Visibility: Quickly determine the state (open/closed) of a defined range of TCP ports on a target system.

Service Discovery: Aid security professionals in identifying exposed network services (like HTTP, SSH, FTP) for auditing purposes.

Audit Automation: Provide a simple, automated script for the initial phase of any vulnerability assessment or penetration test.

✨ Features
Host Resolution: Accepts either an IP address or a hostname (e.g., google.com).

Targeted Scan: Scans ports 1 through 1024 (the Well-Known Ports) by default.

Timeout Handling: Uses a 1.0-second timeout per port to prevent hanging on filtered or non-responsive hosts.

Clear Output: Displays the target IP, scan start time, and a list of all identified OPEN ports.

Duration Tracking: Calculates and reports the total time taken for the scan.

💻 Prerequisites
Python: Version 3.x

Operating System: Any OS with Python installed (Linux, macOS, Windows).

The script uses only the standard built-in Python libraries (socket, sys, datetime), so no external dependencies need to be installed.

⚙️ How to Use
1. Save the Script
Save the provided Python code as a file named port_scanner.py.

2. Run from the Command Line
Execute the script using the Python interpreter:

Bash

python3 port_scanner.py
3. Enter the Target
The script will prompt you to enter the target:

Enter the target IP address or hostname to scan: [TARGET_IP_OR_HOSTNAME]
Example:

To scan a specific IP address: 192.168.1.1

To scan a hostname: testphp.vulnweb.com

4. Example Output
The output will clearly delineate the scan process and results:

--------------------------------------------------
Scanning target: 123.45.67.89
Scan started at: 20:05:30
--------------------------------------------------
Port 21: OPEN
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
...
--------------------------------------------------
Scan finished in 1024.55 seconds.
--------------------------------------------------
🛠️ Technical Details
Key Functions
Function	Purpose
main_scanner()	Handles user input, IP resolution, timing, and iterates through the port range.
scan_port(target_ip, port)	The core scanning logic. Creates a TCP socket and attempts a connection.

Export to Sheets

Socket Implementation
The script uses the standard Python socket library for network communication. Specifically, it employs the TCP connection attempt method:

Socket Type: socket.socket(socket.AF_INET, socket.SOCK_STREAM) specifies an IPv4 (AF_INET) and TCP (SOCK_STREAM) socket.

Connection Test: The s.connect_ex((target_ip, port)) function attempts a TCP connection (SYN packet).

Result Interpretation: If connect_ex returns 0, the port is considered OPEN, indicating a successful TCP Three-Way Handshake


Shutterstock
Explore
was initiated.

Customization
To change the range of ports scanned, modify the start_port and end_port variables within the main_scanner() function:

Python

# Define the range of ports to scan
start_port = 1
end_port = 65535 # To scan all possible TCP ports
