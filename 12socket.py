import scoket
import re

inurl = raw_input("Enter a url likes: 'http://www.py4inf.com/code/romeo.txt'.\n>:")
words = inurl.split('/')
#print words
if words[0].lower() == 'http:' or words[0].lower() == 'https:':
    host = words[2]
else:
    print "Please enter url strats with 'http://' or 'https://'."
    exit()

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if re.search('^http:', inurl):
        mysock.connect((host,80))
        mysock.send('GET '+inurl+' HTTP/1.0\n\n')
    elif re.search('^https:', inurl):
        mysock.connect((host,443))
        mysock.send('GET '+inurl+' HTTPS/1.0\n\n')
except:
    print "Sorry! Thie Enter is invalid."
    exit()
count = 0
length = 0
while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        print 'Received data', 100, '%'
        break
    if count == 0 or count < 3000:
        print data
        count = count + 512
        stuff = re.findall('Content-Length: *([0-9]+)',data)
        if len(stuff) != 1:continue
        summary = int(stuff[0])
    length = length  + len(data)
    number = summary/10
    if 3512 > length > 3000 :
        print '\n\n', 'Starts receiving data', '\n', '... ...'
    elif length > 3000 and (number + 512) > length > number:
        print 'Received data', 10, '%', '\n', '... ...'
    elif length > 3000 and (2*number + 512) > length > 2*number:
        print 'Received data', 20, '%', '\n', '... ...'
    elif length > 3000 and (3*number + 512) > length > 3*number:
        print 'Received data', 30, '%', '\n', '... ...'
    elif length > 3000 and (4*number + 512) > length > 4*number:
        print 'Received data', 40, '%', '\n', '... ...'
    elif length > 3000 and (5*number + 512) > length > 5*number:
        print 'Received data', 50, '%', '\n', '... ...'
    elif length > 3000 and (6*number + 512) > length > 6*number:
        print 'Received data', 60, '%', '\n', '... ...'
    elif length > 3000 and (7*number + 512) > length > 7*number:
        print 'Received data', 70, '%', '\n', '... ...'
    elif length > 3000 and (8*number + 512) > length > 8*number:
        print 'Received data', 80, '%', '\n', '... ...'
    elif length > 3000 and (9*number + 512) > length > 9*number:
        print 'Received data', 90, '%', '\n', '... ...'
if length > 3000:
    print 'This file is has',length,'characters.'
else:
    print 'This file is has',length,'characters.'

mysock.close()
