fname = raw_input('Enter file name\n')
try:
	fhand = open(fname)
except:
	print "File not found"
	exit()
count = 0
for line in fhand:
	if line.startswith("Subject:"):
		count= count +1
print "there were",count,"subject lines in",fname