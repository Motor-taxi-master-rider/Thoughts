import socket
from urllib.request import urlopen

import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9150)
socket.socket = socks.socksocket
print(urlopen('http://icanhazip.com').read())
