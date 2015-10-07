#!/usr/bin/env python
# encoding=utf-8

# getLatestFTP.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 3.2.6 A Client Program FTP Example
#   - Example 3-1. FTP Download Example
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch03/getLatestFTP.py
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch03/getLatestFTP3.py
#   - https://docs.python.org/2/library/ftplib.html


import ftplib
import os
import socket

'''
    from ftplib import FTP
    f = FTP('some.ftp.server')
    f.login('anonymous', 'your@email.address')
    .
    .
    f.quit()
'''

'''
    from ftplib import FTP
    f = FTP('ftp.debian.org')                # connect to host, default port
    f.login()                                # user anonymous, passwd anonymous@
    f.dir()
    f.cwd('debian')                          # change into "debian" directory
    f.dir() or f.retrlines('LIST')           # list directory contents
    f.retrbinary('RETR README', open('README', 'wb').write)
    f.quit()
'''

HOST = 'ftp.debian.org'     # 'ftp.mozilla.org'
DIRN = 'debian'             # 'pub/mozilla.org/webtools'
FILE = 'README.html'        # 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror) as e:
        print 'ERROR: cannot reach "%s"' % HOST  # v2
        # print('ERROR: cannot reach "%s"' % HOST)  # v3
        return

    print '*** Connected to host "%s"' % HOST  # v2
    # print('*** Connected to host "%s"' % HOST)  # v3

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'  # v2
        # print('ERROR: cannot login anonymously')  # v3
        f.quit()
        return

    print '*** Logged in as "anonymous"'  # v2
    # print('*** Logged in as "anonymous"')  # v3

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s" folder' % DIRN  # v2
        # print('ERROR: cannot CD to "%s" folder' % DIRN)  # v3
        f.quit()
        return

    print '*** Changed to "%s"' % DIRN  # v2
    # print('*** Changed to "%s"' % DIRN)  # v3

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
            # retrbinary(cmd, cb[, bs=8192[, ra]])
            # - Download binary file
            # - callback cb for processing each block
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE  # v2
        print('ERROR: cannot read file "%s"' % FILE)  # v3
        if os.path.exists(FILE):
            os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE  # v2
        # print('*** Downloaded "%s" to CWD' % FILE)  # v3

    f.quit()

if __name__ == '__main__':
    main()
