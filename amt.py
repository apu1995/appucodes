amt=float(input("Enter the amount?\n"))
rate=float(input("Enter the rate?\n"))
time=int(input("Enter the time?\n"))

val=0
year=1

while year<=time :
	val=amt+(amt*rate)
	print("Value for year %d is %.2f" % (year,val))
	amt=val
	year=year+1
