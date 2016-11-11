import urllib
from bs4 import BeautifulSoup as BSoup

inurl = raw_input("Enter URL:")
inc = raw_input('Enter count:')
inp = raw_input('Enter position:')
url = inurl
count = 0
while True:
    try:
        uhand = urllib.urlopen(url).read()
        c = int(inc)
        p = int(inp)
    except:
        print "This enter is invalid!"
        break
    if count == 0:print url
    count = count + 1
    position = 0

    soup = BSoup(uhand, "html.parser")
    tags = soup('a')

    for tag in tags:
        position = position + 1
        name =  tag.get_text()
        if position == p:
            #print position, name
            url = tag.get('href', None)
            print url
            break
    if count == c:
        print "Last name in sequence:", name
        break
