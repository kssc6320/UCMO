#! /usr/bin/python3
import socks

s = socks.socksocket()
# Set the proxy
s.set_proxy(socks.SOCKS5, "192.168.20.99", 9000)
# Connect to final destination via the proxy
s.connect(("10.8.0.5", 3333))
s.sendall(b"hello\n")
s.sendall(b"hello again\n")
response = s.recv(2048)
while response:
    print(response)
    response = s.recv(2048)
