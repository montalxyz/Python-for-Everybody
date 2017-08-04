def computepay(h,r):
    if hrs >= 40:
        x = hrs - 40 
        x = x*(10.50*1.5)
        total = x + 40*10.50
    return hrs*10.50

hrs = raw_input("Enter Hours:")
hrs = float(hrs)
p = computepay()
print p