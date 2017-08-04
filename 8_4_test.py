fname = ('romeo.txt')
fh = open(fname)
lst = list()
listline= list()
newlist = list()

for line in fh:

	lst= line.split()
	

	newlist=lst+newlist


	listline.append(lst)
	listline.sort()


newlist.sort()
#create a list with only distinct objects 
finalout = list(set(newlist))
print finalout
