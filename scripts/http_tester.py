# example usage: python3 http_tester.py
# This script looks in every file under public-data-documentation-* to find hyperlink
# When it finds an hyperlink, it does a http request 
# If there is an error, it log it in hyperlink_error.log

import os
import fnmatch
import urllib.request
import re
import logging

# Find every file in a given path
def recursive_glob(rootdir, pattern):
    files = []
    for root, dirnames, filenames in os.walk(rootdir):
        for filenam in fnmatch.filter(filenames, pattern):
            files.append(os.path.join(root, filenam))

    return files

path = ['../public-data-documentation-src/', '../public-data-documentation-md/', '../public-data-documentation-txt/']
pattern='*'
files = []

# If the error log file already exists, delete it
error_log = 'hyperlink_error.log'
if os.path.exists(error_log):
    os.remove(error_log)
logging.basicConfig(filename=error_log ,level=logging.DEBUG)

for j in path:
    files = files + recursive_glob(j, pattern)

link = ''

# Open every file, read them line by line, find hyperlink and test it
for i in files:
    try:
        with open(i) as input_file:
            for line in input_file:
                m = re.search("(?P<url>https?://[^\s]+)", line)
                if m:
                    link = m.group('url')
                    link = link.replace(')', '')
                    link = link.replace(',', '')
                    if link[-1] == '.':
                        link = link[:-1]
                    try:
                        response = urllib.request.urlopen(link)
                    except Exception as e:
                        logging.debug(e)
                        logging.info(link + ' in ' + i)
    except:
        continue