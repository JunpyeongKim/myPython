#!/usr/bin/env python
# encoding=utf-8

# tsTservSS.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.5.1 Creating a SocketServer TCP Server
#   - Example 2-8. SocketServer Timestamp TCP Server
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTservSS.py
#   - Executing
#       - Mac: $ python tsTservSS.py
#       - Ubuntu: $ tsTservSS.py


import SocketServer
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print '...connected from: ', self.client_address
        self.wfile.write('[%s] %s\n' % (
            ctime(), self.rfile.readline().strip())
        )

tcpSerSock = SocketServer.TCPServer(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpSerSock.serve_forever()
