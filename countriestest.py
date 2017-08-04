fhand = open('Countries.txt')
countires = dict() 
nazioni=list()
count= 0
#fhand.rstrip(fhand)



def find():
	count = 0
	for i in fhand:
		count = count + 1
		country = i
		i = i.rstrip('\n')
		if i == yourc:
			print "Found it !"
			print "Number ", count


yourc =raw_input("enter country name")
find()
for i in fhand:
	count = count +1
	i = i.rstrip('\n')
	country = i
	countries=country
	country.rstrip('\n')
	nazioni.append(country)

	if count == 196:
		print "done"
		break
