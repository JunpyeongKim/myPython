#!/usr/bin/env python
# encoding=utf-8

# tsTserv.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.3 Creating a TCP Server
#   - Example 2-1. TCP Timestamp Server
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTserv.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTservV6.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTserv3.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTserv3V6.py
#   - Executing
#       - Mac: $ python tsTserv.py
#       - Ubuntu: $ tsTserv.py


from socket import *
from time import ctime

'''
    ss = socket()                   # create server socket
    ss.bind()                       # bind socket to address
    ss.listen()                     # listen for connections
    inf_loop:                       # server infinite loop
        cs = ss.accept()            # accept client connection
        comm_loop:                  # communication loop
            cs.recv()/cs.send()     # dialog (receive/send)
        cs.close()                  # close client socket
    ss.close()                      # close server socket # (opt)
'''

HOST = ''  # it can use any available address.
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
tcpSerSock = socket(AF_INET, SOCK_STREAM)  # IPv4
# tcpSerSock = socket(AF_INET, SOCK_STREAM)  # IPv6
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)  # simply a maximum number of incoming connection request to accept
                      # before connections are turned away or refused.

while True:
    print 'waiting for connecting...'  # v2
    # print('waiting for connecting...')  # v3
    tcpCliSock, addr = tcpSerSock.accept()  # blocking
    print '...connected from:', addr  # v2
    # print('...connected from:', addr)  # v3

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))  # v2
            # v3: an ASCII bytes "string" rather than in Unicode.
        # # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))  # v3
        # tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))  # v3

    tcpCliSock.close()

tcpSerSock.close()
