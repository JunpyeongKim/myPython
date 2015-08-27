# std_logging.py
# 17.2. logging module
# - http://www.swaroopch.com/notes/python/#logging
# - The best way to further explore the standard library
#   - Doug Hellmann's excellent Python Module of the Week (https://pymotw.com/2/contents.html)


import os, platform, logging


log_dir = 'prj/python/myPython/byteofpython/stdlib'

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), log_dir, 'test.log')
else:
    # platform.platform() --> 'Darwin-14.5.0-x86_64-i386-64bit'
    # os.getenv('HOME') --> /Users/{id}
    logging_file = os.path.join(os.getenv('HOME'), log_dir, 'test.log')

# /Users/{id}/test.log
print "Logging to", logging_file

# configure the logging module
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w'
)

logging.debug('Start of the program')
logging.info('Doing something')
logging.warning('Dying now')