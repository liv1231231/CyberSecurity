import socket
import threading
import concurrent.futures

print_lock = threading.Lock()
ip = input("Enter your the ip of the target: ")


def portscan(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        if sock.connect_ex((ip, port)):
            with print_lock:
                pass

        else:
            with print_lock:
                print(f"Port {port} is open")
    except socket.error or socket.herror or socket.gaierror:
        print("System Exiting...")


with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(65000):
        executor.submit(portscan,ip,port)



