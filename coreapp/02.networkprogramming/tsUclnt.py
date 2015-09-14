#!/usr/bin/env python
# encoding=utf-8

# tsUclnt.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.4.7 Creating a UDP Client
#   - Example 2-7. UDP Timestamp Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsUclnt.py
#   - Executing
#       - Mac: $ python tsUclnt.py
#       - Ubuntu: $ tsUclnt.py


from socket import *

'''
    cs = socket()                   # create client socket
    comm_loop:                      # communication loop
        cs.sendto()/cs.recvfrom()   # dialog (send/receive)
    cs.close()                      # close client socket
'''

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()
