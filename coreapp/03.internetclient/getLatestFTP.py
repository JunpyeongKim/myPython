#!/usr/bin/env python
# encoding=utf-8

# getLatestFTP.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 3.2.6 A Client Program FTP Example
#   - Example 3-1. FTP Download Example
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch03/getLatestFTP.py

import ftplib
import os
import socket

HOST = 'http://ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print 'ERROR: cannot reach "%s"' % HOST
        return

    print '*** Connected to host "%s"' % HOST

    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return

    print '*** Logged in as "anonymous"'

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s" folder' % DIRN
        f.quit()
        return

    print '*** Changed to "%s"' % DIRN

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb').write)
    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % FILE
        if os.path.exists(FILE):
            os.unlink(FILE)
    else:
        print '*** Downloaded "%s" to CWD' % FILE

    f.quit()

if __name__ == '__main__':
    main()
