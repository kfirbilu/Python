import socket
import threading
from queue import Queue

target = '10.0.0.138'


def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET for internet socket, sock_stream for TCP
        sock.connect((target, port))
        return True
    except:
        return False

########## for loop is not efficient, we will use threading instead with queue ##########
# for port in range (1,1024):
#     result = portScan(port)
#     if result:
#         print(f"Port {port} is open!")
#     else:
#         print(f"Port {port} is closed!")



queue = Queue()
open_ports = []

def fillQueue(ports_list):
    for port in ports_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)


port_list=range(1,1024)
fillQueue(port_list)

thread_list = []

for t in range(500):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)


for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)



