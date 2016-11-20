import urllib
import xml.etree.ElementTree as ET

inurl = raw_input('Please enter a url:\n')

try:
    uxml = urllib.urlopen(inurl).read()
except:
    print 'This enter is invalid!'

print 'Retrieving', inurl

tree = ET.fromstring(uxml)
lst = tree.findall('comments/comment/count')

print 'Retrieved', len(uxml), 'characters'
print 'Count:', len(lst)
sumcount = 0
for item in lst:
    nstr = item.find('count').text
    number = int(nstr)
    sumcount = sumcount + number
print 'sum:', sumcount
