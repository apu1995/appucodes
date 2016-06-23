# fibonacci numbers in python.
n=input("Enter number? (>2)")
n1=1
n2=1
print(n1)
print(n2)
n=n-2
while n:
	print(n1+n2)
	temp=n1
	n1=n2
	n2=n1+temp
	n=n-1