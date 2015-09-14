#!/usr/bin/env python
# encoding=utf-8

# tsTservTW.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.6.1 Creating a Twisted Reactor TCP Server
#   - Example 2-10. Twisted Reactor Timestamp TCP Server
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTservTW.py
#   - Executing
#       - Mac: $ python tsTservTW.py
#       - Ubuntu: $ tsTservTW.py


from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567


class TSServeProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from: ', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServeProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
