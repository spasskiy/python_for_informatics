import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')

try:
    html = urllib.urlopen(url).read()
    data = BeautifulSoup(html)
    tags = data('span')
except:
    print 'Provided url is not correct.'
    exit()

sum = 0
count = 0

for tag in tags:
    try:
        sum = sum + int(tag.contents[0])
        count = count + 1
    except:
        print 'No integer in span tag'
        continue

print 'Count', count
print 'Sum', sum
