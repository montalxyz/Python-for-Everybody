# Use the file name mbox-short.txt as the file name
#fname = raw_input("Enter file name: ")
fname="mbox-short.txt"


fh = open(fname)
count = 0
value = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    linevalue = line[20:26]
#    linevalue.lstrip()
    linevalue = float(linevalue)


    value = value + linevalue

avg = value/count

print "Average spam confidence:", avg

