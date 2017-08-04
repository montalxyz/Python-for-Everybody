inph = raw_input("Hours?")
inpr = raw_input("rate ?")
try:
	inph=float(inph)
	inpr=float(inpr)
except:
	inph!=float()
	inpr!=float()
	print("Error, please insert numbers only")
finally:
	if inph >=40:
		over = inph-40
		inph=float(inph)
		overate= inpr * 1.5
		pay = 40*inpr+ overate*over
		print pay
	else : pay = inpr*inph
elif inph !=float() || inpr!=float() :
	print("error")
print (pay)