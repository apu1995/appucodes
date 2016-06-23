# program to see the working of continue in python.
while True:
	n=int(input("Enter an in Integer?"))
	if n<0:
		continue
	elif n==0:
		break
	else:
		print("Square is : %d" %(n*n)) 