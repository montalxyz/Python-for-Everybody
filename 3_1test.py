hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = raw_input("Enter rate:")
rate = float(rate)
if h >= 40:
    above = h-40
    above=float(above)
    extra=rate*1.5
    pay=40*rate+above*extra
else: pay = h * rate

print(pay)