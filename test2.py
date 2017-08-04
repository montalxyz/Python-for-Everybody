largest = None
smallest = None
while True:
	num = raw_input("Enter a number: ")
	
	try:
		num = int(num)
		if num > largest:
			largest = num
		elif smallest < num: 
				smallest = num

	except ValueError:
		print "Invalid input"
	if num == "done" : break


print "Maximum is", largest 
print "Minimum is",	smallest