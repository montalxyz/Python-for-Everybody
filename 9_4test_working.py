#9.4 Write a program to read through the mbox-short.txt and figure out
#looks for 'From ' lines and takes the second word of those lines as
# the person who sent the mail. The program creates a Python dictionary
# that maps the sender's mail address to a count of the number of times
#they appear in the file. After the dictionary is produced, the program
#reads through the dictionary using a maximum loop to find the most
#prolific committer.
#

#     ORIGINAL CODE
#name = raw_input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
#handle = open(name)





##########
name = 'mbox-short.txt'

handle = open(name)
text = handle.read()
sender = dict()
pop = None
freq = 0

infile = open('mbox-short.txt').readlines()
for line in infile:
	if line.startswith("From "):

		line.strip()
		line =line.split()
		email=line[1]
#all fine to here


		##
		if email in sender:
			x = sender.get(email)
			sender[email]= x +1
			if x >= freq:
				freq = x +1

			else:
				continue

		elif email not in sender:
			sender[email]=1

		#
	else:
		continue
############


############
#max(sender, key=lambda i:sender[i])
#asdd = max(sender, key=lambda i:sender[i])
#r = sender.get(asd)
#xg =
#xg = sender.get[asdd]
#xg = sender.get(asdd)
#int(xg)
#print sender, freq
#print asdd,xg
########

hello = max(sender, key=sender.get)
world =  stats[max(stats, key=stats.get)]

print hello, world
