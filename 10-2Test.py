#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = 'mbox-short.txt'
handle = open(name)
text = handle.read()
hourcounts = dict()

freq = 0

infile = open('mbox-short.txt').readlines()
for line in infile:
	if line.startswith("From "):

		line.strip()
		line =line.split()
		#print line
		time=line[5]
		hour= time[0:2]
		#print hour

		x = hour
		y = int(x)

#		if hour in x:
#			y= y+ 1
#			print y

		for i in hour:
			hourcounts[hour]= hourcounts.get(hour,0)+1
			


lst = list()
for key, val in hourcounts.items():
	lst.append( (key, val/2) )

lst.sort(reverse=False)

for val, key in lst:
	print val , key
