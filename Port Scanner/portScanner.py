import socket
import threading
from queue import Queue

hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

print(f"Scanning open ports for {hostname}")
print(f"Local IP address is: {local_ip}")


def TCPportScan(port):
    try:
        sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET for internet socket, sock_stream for TCP
        sockTCP.connect((local_ip, port))
        sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET for internet socket, sock_dgram for UDP
        sockUDP.connect((local_ip, port))
        return True
    except:
        return False


def UDPportScan(port):
    try:
        sockUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET for internet socket, sock_dgram for UDP
        sockUDP.connect((local_ip, port))
        return True
    except:
        return False


queue = Queue()
open_tcp_ports = []
open_udp_ports = []


def fillQueue(ports_list):
    for port in ports_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if TCPportScan(port):
            open_tcp_ports.append(port)

        if UDPportScan(port):
            open_udp_ports.append(port)


port_list = range(1, 9999)  # specify port range to test
fillQueue(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open TCP ports are: ", open_tcp_ports)

print("Open UDP ports are: ", open_udp_ports)

