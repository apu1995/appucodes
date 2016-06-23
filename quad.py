# finding roots of a quadratic function.

import math
a=int(input("Enter a?"))
b=int(input("Enter b?"))
c=int(input("Enter c?"))

d=b*b-4*a*c
if d<0:
	print("Roots are imaginary.")
else:
	r1=(-b+math.sqrt(d))/2.0*a
	r2=(-b-math.sqrt(d))/2.0*a

print("The roots are %d and %d "%(r1,r2))


# trying else if

x=3
if x<0:
	print('0')
elif x==3:
	print("here")
else:
	print("haha")

