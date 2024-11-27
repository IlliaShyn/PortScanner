import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set timeout to 1 second
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"[+] Port {port} is open on {host}")
    except Exception as e:
        print(f"[-] Error scanning port {port}: {e}")


def main():
    host = input("Enter the target host (e.g., IP or domain): ")
    start_port = int(input("Enter the starting port (e.g., 1): "))
    end_port = int(input("Enter the ending port (e.g., 1024): "))

    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)


if __name__ == "__main__":
    main()
