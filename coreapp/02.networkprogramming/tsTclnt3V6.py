#!/usr/bin/env python
# encoding=utf-8

# tsTclnt3V6.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.4 Creating a TCP Client
#   - Example 2-4. Python 3 TCP Timestamp Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclnt3V6.py
#   - Executing
#       - Mac: $ python tsTclnt3V6.py
#       - Ubuntu: $ tsTclnt3V6.py


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
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()