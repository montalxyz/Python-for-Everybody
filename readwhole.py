filehandle = open('Untitled.txt')
inp = filehandle.read()
print len(inp)


print "first 19 chars", inp[:20]