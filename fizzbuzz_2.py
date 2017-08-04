x = range(101)
for i in x:

	if i%2 == 0 and i%5 == 0:
		print i,"Fizz Buzz"
	elif i%5 == 0:
		print i,"Buzz"
	elif i%2 == 0:
		print i,"Fizz"
	elif i%2 != 0 and i%5 != 0:
		print i,"nope"