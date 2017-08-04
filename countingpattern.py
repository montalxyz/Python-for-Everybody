counts = dict()
print"enter line of text"
line = raw_input('')

words=line.split()
print 'words',words

print 'counting'
for word in words:
	counts[word]=counts.get(word,0)+1
print 'counts',counts