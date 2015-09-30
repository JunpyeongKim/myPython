#!/usr/bin/env python
# encoding=utf-8

# getFirstNNTP.py

# Core Python Application Programming 3E, Wesley J. Chun
# - 3.3.6 A Client Program NNTP Example
#   - Network News Transfer Protocol
#   - Example 3-2. NNTP Download Example
#       - http://cpp.wesc.webfactional.com/cpp3ev2/book3v2/ch03/getFirstNNTP.py
#   - https://docs.python.org/2/library/nntplib.html?highlight=nntp#module-nntplib


import nntplib
import socket

'''
    from nntplib import NNTP
    s = NNTP('news.gmane.org')
    resp, count, first, last, name = s.group('gmane.comp.python.committers')
    print 'Group', name, 'has', count, 'articles, range', first, 'to', last
    resp, subs = s.xhdr('subject', first + '-' + last)
    for id, sub in subs[-10:]: print id, sub
    s.quit()
'''

HOST = 'news.gmane.org'  # 'your.nntp.server'
GRNM = 'gmane.comp.python.committers'  # 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNeverGuess"


def main():
    try:
        n = nntplib.NNTP(HOST)  #, user=USER, password=PASS)
    except socket.gaierror as e:
        print('ERROR: cannot reach host "%s"' % HOST)
        print('    ("%s")' % eval(str(e))[1])
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR: access denied on "%s"' % HOST)
        print('    ("%s")' % str(e))
        return

    print('*** Connected to host "%s"' % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: cannot connect to group "%s"' % GRNM)
        print('    ("%s")' % str(e))
        print('    Server may require authentication')
        print('    Uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPTemporaryError as e:
        print('ERROR: group "%s" unavailable' % GRNM)
        print('    ("%s")' % str(e))
        n.quit()
        return

    print('*** Found newsgroup "%s"' % GRNM)

    # xhdr() returns a 2-tuple consisting of
    # a server response (rsp) and a list of the headers in the range we specify.
    #   - Because we are only requesting this information for one message (the last one),
    #     just take the first element of the list (hdr[0]).
    #       - That data item is a 2-tuple consisting of the article number and the data string.
    #   - Because we already know the article number (we give it in our range request),
    #     we are only interested in the second item, the data string (hdr[0][1]).
    rng = '%s-%s' % (lst, lst)
    rsp, frm = n.xhdr('from', rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)

    print('''*** Found last article (#%s):
    From: %s
    Subject: %s
    Date: %s
    ''' % (lst, frm[0][1], sub[0][1], dat[0][1]))

    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()


def displayFirst20(data):
    print('*** First (<= 20) meaningful lines:\n')

    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True

    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not lower.startswith('>>>')) or \
                lower.startswith('|') or \
                lower.startswith('in article') or \
                lower.endswith('writes:') or \
                lower.endswith('wrote:'):
                continue

        # If there is more than one blank line consecutively, only show the first one
        if not lastBlank or (lastBlank and line):
            print('    %s' % line)
            if line:
                count += 1
                lastBlank = False
            else:
                lastBlank = True

        if count == 20:
            break

if __name__ == '__main__':
    main()

