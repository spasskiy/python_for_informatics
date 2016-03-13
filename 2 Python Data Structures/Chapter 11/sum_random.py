#!/etc/bin/local/python

import re

try:
    name = raw_input("Enter file:")
    if len(name) < 1:
        name = "regex_sum_243227.txt"
    handle = open(name)
except:
    print 'Cannot open', name, 'file'
    exit()

numbers_lists = list()
numbers = list()

for line in handle:
    if re.search('[0-9]+', line):
        for number in re.findall('[0-9]+', line):
            numbers.append(int(number))

print sum(numbers)