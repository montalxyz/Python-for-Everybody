import re

hand = open('regex_sum_290754.txt')
total = 0
derp =[]
#for line in hand:
#	goal = re.findall([0-9]*'233')
#	print goal
x = list()

for line in hand:
	line = line.rstrip()
	#if re.search('\s([0-9]+?\s)', line) :
	numbrs = re.findall('[0-9]+', line) 
	derp= derp + numbrs

for n in derp:
	total= total + float(n)

print total

#print x