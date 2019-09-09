binary=bin(17)
binary=binary[2:]

n=len(binary)
count=1
c1=[0]*(n+1)
c0=[0]*(n+1)

for i in range(n):
    if binary[i]=='0':
        c1[i+1]=c1[i]
        c0[i+1]=c0[i]+1
    else:
        c1[i+1]=c1[i]+1
        c0[i+1]=c0[i]

for i in range(n):
	for j in range(i+1,n+1):
		print(binary[i:j]," ",count,end=" ")
		print("Ones:",c1[j]-c1[i],"Zeros:",c0[j]-c0[i])
		count=count+1