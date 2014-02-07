from bs4 import BeautifulSoup
import urllib2
import re
 
url = "https://hasjob.co"
 
content = urllib2.urlopen(url).read()
 
soup = BeautifulSoup(content)
 
test = soup.find_all('li')
print test 
