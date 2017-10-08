import time
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

def benchmark(addr,nmessages):
    sock=socket(AF_INET,SOCK_STREAM)
    sock.connect(addr)
    start=time.time()
    for n in range(nmessages):
        sock.send(b'x')
        resp=sock.recv(10000)
    end=time.time()
    print(nmessages/(end-start),'message/sec')

benchmark(('localhost',25000),100000)