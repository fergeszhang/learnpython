import urllib
from bs4 import BeautifulSoup as BSoup

while True:
    inurl = raw_input("Please enter a url likes: 'http://www.dr-chuck.com/page1.htm' or over with 'done'.\n>:")
    if inurl == "done":break
    try:
        uhand = urllib.urlopen(inurl).read()
    except:
        print "This enter is invalid!"
        continue
    soup = BSoup(uhand, "html.parser")

    tags = soup('a')
    print "\nThese are parsed result:"
    for tag in tags:
        print tag.get("href", None)
    print "DONE\n\n"
