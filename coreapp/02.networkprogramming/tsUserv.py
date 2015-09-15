#!/usr/bin/env python
# encoding=utf-8

# tUserv.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.6 Creating a UDP Server
#   - Example 2-6. UDP Timestamp Server
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsUserv.py
#   - Executing
#       - Mac: $ python tsUserv.py
#       - Ubuntu: $ tsUserv.py


from socket import *
from time import ctime

'''
    ss = socket()                           # create server socket
    ss.bind()                               # bind server socket
    inf_loop:                               # server infinite loop
        cs = ss.recvfrom()/ss.sendto()      # dialog (receive/send)
    ss.close()                              # close server socket
'''

HOST = ''
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
udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print 'waiting for message...'  # Note: as opposed to "waiting for connection"
        data, addr = udpSerSock.recvfrom(BUFSIZ)  # (passively) wait for a message (a datagram)
        udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
        print '...received from and returned to: ', addr
except KeyboardInterrupt:
    print 'except...KeyboardInterrupt'
else:
    print 'else...'
finally:
    print 'finally...'
    udpSerSock.close()
