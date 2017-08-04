largest = None
smallest = None	

def check():
	if num > 1 and num > largest:
		largest = num
	if num < smallest:
		smallest = num




while True:
	num = raw_input("Enter a number: ")
	if num != type(int) and num != "done":
		print "Invalid input"
	elif num == type(int) and num > largest:
		largest = num
	elif num == type(int) and num < smallest:
		smallest = num


	elif num == "done" : break

print "Maximum is", largest
print "Minimum is", smallest