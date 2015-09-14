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

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print '...received from ana returned to: ', addr

udpSerSock.close()
