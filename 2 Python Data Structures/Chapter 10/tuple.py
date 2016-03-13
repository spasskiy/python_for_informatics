#!/etc/bin/local/python

try:
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name, 'r')
except:
    print 'Cannot open %s file' % name
    exit()

hours = dict()

for line in handle:
    if line.strip().startswith('From '):
        words = line.strip().split()
        hour = words[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

lst = list()

for k, v in hours.items():
    lst.append((k, v))

for k, v in sorted(lst):
    print k, v
