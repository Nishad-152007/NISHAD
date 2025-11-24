#Basic Port Scanner. 

import socket
import sys
from datetime import datetime

def scan_port(target_ip, port):
    """
    Attempts to connect to a specific TCP port on the target IP.
    Returns True if the port is open, False otherwise.
    """
    # Create a socket object (AF_INET for IPv4, SOCK_STREAM for TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set a timeout for the connection attempt
    s.settimeout(1.0) # 1 second timeout

    try:
        # Attempt to connect to the target IP and port
        result = s.connect_ex((target_ip, port))
        
        # connect_ex returns 0 if the connection is successful (port is open)
        if result == 0:
            print(f"Port {port}: OPEN")
            return True
        else:
            # Optionally, you can print closed ports, but often left out for clean output
            # print(f"Port {port}: Closed")
            return False

    except socket.gaierror:
        # Handle error if the hostname/IP address couldn't be resolved
        print("Hostname could not be resolved. Exiting.")
        sys.exit()
    
    except socket.error:
        # Handle general socket errors
        print("Couldn't connect to server.")
        sys.exit()
        
    finally:
        # Always close the socket connection
        s.close()

def main_scanner():
    """
    Main function to get input and start the scan.
    """
    
    # Get the target input (allows hostname or IP address)
    target = input("Enter the target IP address or hostname to scan: ")
    
    # Resolve hostname to IPv4 address
    try:
        # This resolves the hostname (e.g., 'google.com') to an IP
        target_ip = socket.gethostbyname(target) 
    except socket.gaierror:
        print("Error: Invalid hostname or IP address.")
        return

    print("-" * 50)
    print(f"Scanning target: {target_ip}")
    print(f"Scan started at: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 50)

    # Define the range of ports to scan
    start_port = 1
    end_port = 1024 # Scanning common ports up to 1024 (Well-known ports)

    # Start the scanning loop
    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

    # Calculate and print scan duration
    end_time = datetime.now()
    duration = end_time - datetime.now().replace(hour=int(datetime.now().strftime('%H')), minute=int(datetime.now().strftime('%M')), second=int(datetime.now().strftime('%S')), microsecond=0)
    
    print("-" * 50)
    print(f"Scan finished in {duration.total_seconds():.2f} seconds.")
    print("-" * 50)

# Execute the main function
if __name__ == "__main__":
    main_scanner()