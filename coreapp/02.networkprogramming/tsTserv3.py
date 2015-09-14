#!/usr/bin/env python
# encoding=utf-8

# tsTserv3.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.3 Creating a TCP Server
#   - Example 2-2. Python 3 TCP Timestamp Server
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTserv3.py
#   - Executing
#       - Mac: $ python tsTserv3.py
#       - Ubuntu: $ tsTserv3.py


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

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connecting...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        # tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

    tcpCliSock.close()

tcpSerSock.close()
