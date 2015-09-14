#!/usr/bin/env python
# encoding=utf-8

# tsTclntTW.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 2.6.2 Creating a Twisted Reactor TCP Client
#   - Example 2-11. Twisted Reactor Timestamp TCP Client
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch02/tsTclntTW.py
#   - Executing
#       - Mac: $ python tsTclntTW.py
#       - Ubuntu: $ tsTclntTW.py


from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 21567


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('> ')
        if data:
            self.transport.write(data)
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
