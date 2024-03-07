import time
import signal
import socket

def run_remote_server_C():
    sock_remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_remote.bind(('137.110.33.228', 54321)) # TODO: replace with Connor's IPv4 addr thru VPN
    sock_remote.listen()
    conn_remote, addr_remote = sock_remote.accept()
    with conn_remote:
        print("before remote C")
        sock_pynq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.0001)
        sock_pynq.connect(('192.168.2.99', 54321))
        while True:
            time.sleep(0.0001)
            data_remote = conn_remote.recv(1024)
            if (data_remote.decode() == 'disconnect'):
                print("disconnect remote C")
                sock_pynq.sendall(b'disconnect')
                break
            elif (data_remote.decode() == 'blue'):
                print("blue remote C")
                sock_pynq.sendall(b'blue')
            elif (data_remote.decode() == 'green'):
                print("green remote C")
                sock_pynq.sendall(b'green')
            elif (data_remote.decode() == 'red'):
                print("red remote C")
                sock_pynq.sendall(b'red')
        sock_pynq.close()
    print("after remote C")

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    run_remote_server_C()
