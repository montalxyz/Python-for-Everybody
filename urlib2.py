import urllib
fhand = urllib.urlopen('http://www.yourpageurlgoes.here/page.htm')

for line in fhand:
	print line.strip()
	