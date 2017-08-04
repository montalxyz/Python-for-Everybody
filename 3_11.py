rate = 0
hrs = 0
pay = 0

hrs = raw_input("hours ?")
x =float(hrs)
rate= raw_input("paY ?")
y =float(rate)

if x >= 40:
	base = 0.00
	nx = x-40.0
	nr = 1.5* y
	extrapay = nx * nr
	base = 40.0 * y
	payextra = base +extrapay
	print payextra
else:
	pay =x*y
	print pay