def computepay(h,r):
    if h >= 40:
        x = h - 40 
        x = x*(10.50*1.5)
        t = x + 40*10.50
    return t

h = raw_input("Enter Hours:")
h = float(h)
r = 10.50
p = computepay(h,r)
print p