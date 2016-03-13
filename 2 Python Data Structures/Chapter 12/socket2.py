import httplib


connect = httplib.HTTPConnection('www.pythonlearn.com')
connect.request('GET', '/code/intro-short.txt')
headers = connect.getresponse().getheaders()
headers_to_check = ['Last-Modified', 'ETag', 'Content-Length', 'Cache-Control', 'Content-Type']

headers_to_check_mod = []

for header in headers_to_check:
    headers_to_check_mod.append(header.lower())

for header in headers:
    if header[0].lower() in headers_to_check_mod:
        print '%s: %s' % (header[0], header[1])

connect.close()
