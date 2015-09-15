#!/usr/bin/env python
# encoding=utf-8

# tsTclnt.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.4 Creating a TCP Client
#   - Example 2-3. TCP Timestamp Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclnt.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclntV6.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclnt3.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclnt3V6.py
#   - Executing
#       - Mac: $ python tsTclnt.py
#       - Ubuntu: $ tsTclnt.py


from socket import *

'''
    cs = socket()               # create client socket
    cs.connect()                # attempt server connection
    comm_loop:                  # communication loop
        cs.send()/cs.recv()     # dialog (send/receive)
    cs.close()
'''

HOST = '127.0.0.1'  # IPv4
# HOST = 'localhost'  # IPv4
# HOST = '::1'  # IPv6
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

'''
    socket.socket(socket_family, socket_type, protocol=0)
    - socket_family: socket.AF_INET/AF_UNIX
    - socket_type: socket.SOCK_STREAM/SOCK_DGRAM

    e.g. tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
'''
tcpCliSock = socket(AF_INET, SOCK_STREAM)  # IPv4
# tcpCliSock = socket(AF_INET6, SOCK_STREAM)  # IPv6
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')  # v2
    # data = input('> ')  # v3
    if not data:
        break
    tcpCliSock.send(data)  # v2
    # tcpCliSock.send(bytes(data, 'utf-8'))  # v3
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data  # v2
    # print(data.decode('utf-8'))  # v3; have to decode the string that comes from the server.

tcpCliSock.close()
