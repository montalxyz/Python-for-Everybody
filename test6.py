text = "X-DSPAM-Confidence:    0.8475";

startposition = text.find("0")
number = text[startposition : ]


float(number)
print number