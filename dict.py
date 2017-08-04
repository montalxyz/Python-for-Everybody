d = dict()
d['asd']=True
d['fury']=True
print d
x = raw_input("new name:")
if x in d ==True:
	print "already there"
else:
	d[x]= True

	print d
	print "done"