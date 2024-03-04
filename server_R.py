import time
import signal
import socket

def run_server_R():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.2.1', 54321))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print("before R")
        sock_remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.0001)
        sock_remote.connect(('127.0.0.1', 54321)) # TODO: replace with Connor's IPv4 addr thru VPN
        while True:
            print("inside R")
            time.sleep(0.0001)
            data = conn.recv(1024)               
            if (data.decode() == 'disconnect'):
                print("disconnect R")
                sock_remote.sendall(b'disconnect')
                break
        sock_remote.close()
    print("after R")

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    run_server_R()
