import socket
import re
import time

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
text = ""
print "\nStarts receiving data.\n... ..."
while True:
    data = mysock.recv(5120)
    time.sleep(0.25)
    if (len(data) < 1):
        print 'Received data', 100, '%\n'
        break
    if count == 0 or count < 3000:
        #print data
        count = count + 5120
        stuff = re.findall('Content-Length: *([0-9]+)',data)
        if len(stuff) != 1:continue
        summary = int(stuff[0])
    length = length  + len(data)
    number = summary/10
    text = text + data
    if (number + 5120) > length > number:
        print 'Received data', 10, '%', '\n', '... ...'
    elif (2*number + 5120) > length > 2*number:
        print 'Received data', 20, '%', '\n', '... ...'
    elif (3*number + 5120) > length > 3*number:
        print 'Received data', 30, '%', '\n', '... ...'
    elif (4*number + 5120) > length > 4*number:
        print 'Received data', 40, '%', '\n', '... ...'
    elif (5*number + 5120) > length > 5*number:
        print 'Received data', 50, '%', '\n', '... ...'
    elif (6*number + 5120) > length > 6*number:
        print 'Received data', 60, '%', '\n', '... ...'
    elif (7*number + 5120) > length > 7*number:
        print 'Received data', 70, '%', '\n', '... ...'
    elif (8*number + 5120) > length > 8*number:
        print 'Received data', 80, '%', '\n', '... ...'
    elif (9*number + 5120) > length > 9*number:
        print 'Received data', 90, '%', '\n', '... ...'
mysock.close()
pos = text.find("\r\n\r\n")
print "Header length", pos
print 'This file is has',length,'characters.'
print text[(pos + 4):(3004 + pos)]
