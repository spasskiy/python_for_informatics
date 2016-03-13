import urllib
from BeautifulSoup import *

try:
    count = int(raw_input('Enter count: '))
    position= int(raw_input('Enter position: '))
except:
    print 'An integer should be entered'
    exit()

for i in range(count + 1):
    try:
        url = tags[position - 1].get('href', None)
    except:
        url = raw_input('Enter URL: ')
    print 'Retrieving:', url
    html = urllib.urlopen(url).read()
    data = BeautifulSoup(html)
    tags = data('a')
