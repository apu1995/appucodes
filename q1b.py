import string
test=raw_input("Enter the test string?")
allchars=string.printable
flag=1
for c in test:
	if c in allchars:
		allchars=allchars.replace(c,"")
	else:
		flag=0

if(flag==0):
	print "Not All Characters are Unique."
else:
	print "All Unique Characters."
