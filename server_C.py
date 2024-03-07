import time
import signal
import socket

def run_server_C():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.2.1', 12345))
    sock.listen()
    conn, addr = sock.accept()
    with conn:
        print("before C")
        sock_remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(0.0001)
        sock_remote.connect(('137.110.38.247', 12345)) # TODO: replace with Ramin's IPv4 addr thru VPN
        while True:
            time.sleep(0.0001)
            data = conn.recv(1024)               
            if (data.decode() == 'disconnect'):
                print("disconnect C")
                sock_remote.sendall(b'disconnect')
                break
            elif (data.decode() == 'blue'):
                print("blue C")
                sock_remote.sendall(b'blue')
            elif (data.decode() == 'green'):
                print("green C")
                sock_remote.sendall(b'green')
            elif (data.decode() == 'red'):
                print("red C")
                sock_remote.sendall(b'red')
        sock_remote.close()
    print("after C")

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit)
    run_server_C()
