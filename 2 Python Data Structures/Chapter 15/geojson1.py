from __future__ import print_function
import urllib
import json

address = ''
while len(address) < 1:
    address = raw_input('Enter location: ')

params = {'sensor': 'false', 'address': address}
url = 'http://python-data.dr-chuck.net/geojson?' + urllib.urlencode(params)

try:
    print('Retrieving {}'.format(url))
    json_data = urllib.urlopen(url).read()
    print('Retrieved {} characters'.format(len(json_data)))
except:
    print('URL is not valid.')
    exit()

try:
    data = json.loads(json_data)
#    print(json.dumps(data, indent=2))
except:
    print('JSON is not valid.')
    exit()

if ('status' in data) and data['status'] == 'OK':
    for result in data['results']:
        print(result['place_id'])
elif 'error' in data:
    print(data['error'])
else:
    print('Unknown error.')
