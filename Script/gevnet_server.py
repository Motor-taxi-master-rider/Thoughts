from gevent.server import StreamServer


# this handler will be run for each incoming connection in a deficated greenlet

def echo(socket, address):
    print('New connection from {}'.format(address))
    while True:
        data = socket.recv(100000)
        if not data:
            break
        socket.sendall(b'Got:' + data)
    socket.close()


if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 25000), echo)
    server.serve_forever()
