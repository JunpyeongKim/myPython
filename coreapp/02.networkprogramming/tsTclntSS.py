#!/usr/bin/env python
# encoding=utf-8

# tsTclntSS.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.5.2 Creating a SocketServer TCP Client
#   - Example 2-9. SocketServer Timestamp TCP Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclntSS.py
#   - Executing
#       - Mac: $ python tsTclntSS.py
#       - Ubuntu: $ tsTclntSS.py


from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    # The default behavior of the SocketServer request handler is
    # to accept connection, get the request, and then close the connection.
    # This makes it so that we cannot keep our connection
    # throughout the execution of our application,
    # so we need to create a new socket each time we send a message to the serer.
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data + '\n')
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
    tcpCliSock.close()

if tcpCliSock:
    print 'tcpCliSock...'
    tcpCliSock.close()
else:
    print 'not tcpCliSock'