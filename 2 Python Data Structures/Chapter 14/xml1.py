import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')

try:
    print 'Retrieving {}'.format(url)
    data = urllib.urlopen(url).read()
    print 'Retrieved {} characters'.format(len(data))
    xml_data = ET.fromstring(data)
except:
    print 'URL is not valid.'

xml_data.findall('comment')

sum, count = 0, 0
comments = xml_data.findall('.//comment/count')
for comment in comments:
    sum = sum + int(comment.text)
    count = count + 1

print 'Count:', count
print 'Sum:', sum
