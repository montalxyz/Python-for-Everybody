# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
text = fh.read()
output = text
for line in output:
   if line.startswith("and mind-numbing"):
            line.rstrip()
print output.upper()
