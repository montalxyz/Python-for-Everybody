inph = raw_input("Hours?")
inpr = raw_input("rate ?")
inph=float(inph)
inpr=float(inpr)
if inph >=40:
	over = inph-40
	inph=float(inph)
	overate= inpr * 1.5
	pay = 40*inpr+ overate*over
	print pay
else : pay = inpr*inph
print (pay)