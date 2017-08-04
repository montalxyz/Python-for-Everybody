import socket
import re
import operator


def f3(seq):
   # Not order preserving
	keys = {}
	for e in seq:
		keys[e] = 1
	return keys.keys()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com', 80))

mysock.send('GET http://www.pythonlearn.com/ HTTP/1.0\n\n')
counts = dict()
chars=list()
n=0

while True:
	data = mysock.recv(512)
	if ( len(data)<1):
		break
	
	if re.search('.', data):
		n=n+1
	newdata=data
	for i in newdata:
		counts[i] = counts.get(i,0)+1
		chars.append(i)




	#print newdata

print f3(chars)

mysock.close()