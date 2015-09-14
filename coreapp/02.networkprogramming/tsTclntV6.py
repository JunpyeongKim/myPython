#!/usr/bin/env python
# encoding=utf-8

# tsTclntV6.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.4 Creating a TCP Client
#   - Example 2-5. IPv6 TCP Timestamp Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclntV6.py
#   - Executing
#       - Mac: $ python tsTclntV6.py
#       - Ubuntu: $ tsTclntV6.py

from socket import *

'''
    cs = socket()               # create client socket
    cs.connect()                # attempt server connection
    comm_loop:                  # communication loop
        cs.send()/cs.recv()     # dialog (send/receive)
    cs.close()
'''

HOST = '::1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET6, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data

tcpCliSock.close()