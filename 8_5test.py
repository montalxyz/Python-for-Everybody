fname = ('mbox-short.txt')
if len(fname) < 1 : fname = "mbox-short.txt"
    
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()

    if line.startswith('From '): 
        count = count + 1
        line = line.split()
        print line[1]

print "There were", count, "lines in the file with From as the first word"