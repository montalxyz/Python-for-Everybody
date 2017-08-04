# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = ('http://python-data.dr-chuck.net/known_by_Dorian.html')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count=0
repeat= 7
# Retrieve all of the anchor tags
tags = soup('a')
trigger = True
reps= 7


while trigger==True and repeat >=0:
	for tag in tags:
		x= tag.get('href', None)
		count=count+1
		if count <= 18:
			trigger = trigger
			print 'ongoing'
		elif count >= 18:
			trigger= False
			url=x
			
if trigger == False:
	print x
	count = 0

	reps=reps-1
	print 'repetitions',reps
	trigger = True

		
