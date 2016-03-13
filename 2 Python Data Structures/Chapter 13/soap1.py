import urllib2
from BeautifulSoup import *

url = 'https://yandex.ru/search/?lr=213&text=oscar+2016'.encode('ascii')

html = urllib2.urlopen(url).read()
soap = BeautifulSoup(html)

tags = soap('script')

for tag in tags:
    print tag.get('src', None)
