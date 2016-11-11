import urllib
from bs4 import BeautifulSoup

inurl = raw_input('Enter - url:')
words = inurl.split('/')

try:
    uhand = urllib.urlopen(inurl)
except:
    print 'This url is invalid!'
    exit()

headers =  uhand.info()
size = headers.getheader('Content-Length')
count = dict()
length = 0
for line in uhand:
    if length < 3000:
        print line.rstrip()
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0)
    length = length + len(line)

print '\n\n', "This web is", length, "characters."
