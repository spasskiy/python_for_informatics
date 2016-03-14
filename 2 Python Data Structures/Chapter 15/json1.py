from __future__ import print_function
import urllib
import json

url = raw_input('Enter location: ')

try:
    print('Retrieving {}'.format(url))
    json_data = urllib.urlopen(url).read()
    print('Retrieved {} characters'.format(len(json_data)))
except:
    print('URL is not valid.')

try:
    data = json.loads(json_data)
except:
    print('JSON is not valid.')

sum, count, chars = 0, 0, 0

for comment in data['comments']:
    sum = sum + comment['count']
    count = count + 1

print('Count:', count)
print('Sum:', sum)