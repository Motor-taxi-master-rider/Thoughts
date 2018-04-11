import time
from socket import AF_INET, SO_REUSEADDR, SOCK_STREAM, SOL_SOCKET, socket


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
