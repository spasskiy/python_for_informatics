#!/etc/bin/local/python

import re

fopen = open('mbox-short.txt')
emails = dict()


for line in fopen:
    line = line.strip()
    if line.startswith('From '):
        print line
        emails[re.findall('^From (\S+?@\S+)', line)[0]] = emails.get(re.findall('^From (\S+?@\S+)', line)[0], 0) + 1

print emails
