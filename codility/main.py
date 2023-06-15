import socket
import re


class PortScanner:
    def scan(self, ip: str, udp: bool, from_port: int, to_port: int) -> dict[int, bool]:
        ip_pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

        if not re.match(ip_pattern, ip):
            return {}

        protocol = "UDP" if udp else "TCP"
        print(f"Scanning {ip} using {protocol} protocol...")

        open_ports = {}

        for port in range(from_port, to_port + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
                sock.settimeout(2)

                if sock.connect_ex((ip, port)) == 0:
                    open_ports[port] = True
                    print(f"Port {port} is open")
                else:
                    open_ports[port] = False
                    print(f"Port {port} is closed")

            except socket.error as e:
                print(f"Could not connect to {ip}:{port} - {e}")

            finally:
                sock.close()

        return open_ports


scanner = PortScanner()
scanner.scan('127.0.0.1', False, 3300, 3309)
