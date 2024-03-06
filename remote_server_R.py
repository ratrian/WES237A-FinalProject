import time
import signal
import socket

def run_remote_server_R():
    sock_remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_remote.bind(('137.110.32.55', 12345)) # TODO: replace with Ramin's IPv4 addr thru VPN
    sock_remote.listen()
    conn_remote, addr_remote = sock_remote.accept()
    with conn_remote:
        print("before remote R")
        sock_pynq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.0001)
        sock_pynq.connect(('192.168.2.99', 12345))
        while True:
            time.sleep(0.0001)
            data_remote = conn_remote.recv(1024)
            if (data_remote.decode() == 'disconnect'):
                print("disconnect remote R")
                sock_pynq.sendall(b'disconnect')
                break
            sock_pynq.sendall(data_remote)
        sock_pynq.close()
    print("after remote R")

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    run_remote_server_R()
