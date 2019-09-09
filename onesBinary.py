def onesBinary(n):
	count=0
	while(n>0):
		if n&1==1:
			count=count+1
		n=n>>1
	return count

print(onesBinary(1))
print(onesBinary(2))
print(onesBinary(0))
print(onesBinary(9))