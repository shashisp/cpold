import urllilb2
response = urllib2.urlopen('https://hasjob.co/')
print response.info()
html = response.read()
print "Jobs :", html
response.close()
