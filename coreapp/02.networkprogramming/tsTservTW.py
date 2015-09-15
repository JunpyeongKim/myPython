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


# Twisted
# - a complete event-driven networking framework --> asynchronous
# - twisted.internet : Twisted's Internet component
#   - protocol & reactor : its subpackages
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

# The transport instance is how we can communicate with the client.
class TSServProtocol(protocol.Protocol):
    """Timestamp Server Class.

    """

    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from: ', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))

# It is called a factory
# because an instance of our protocol is "manufactured" every time we get an incoming connection.
factory = protocol.Factory()
# when it receives a request, it creates a TSServProtocol instance to take care of that client.
factory.protocol = TSServProtocol
print 'waiting for connection...'
reactor.listenTCP(PORT, factory)
reactor.run()
