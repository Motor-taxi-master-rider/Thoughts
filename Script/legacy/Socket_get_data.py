import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.py4inf.com', 80))
a='GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'
mysock.send(a.encode())

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data);


mysock.close()
