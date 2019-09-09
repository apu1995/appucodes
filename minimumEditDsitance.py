def minimumEditDistance(s1,s2):
	l1=len(s1)
	l2=len(s2)
	changes=[[0 for j in range(l2+1)] for i in range(l1+1)]

	for i in range(l1+1):
		changes[i][0]=i

	for j in range(l2+1):
		changes[0][j]=j

	for i in range(1,l1+1):
		for j in range(1,l2+1):

			if s1[i-1]==s2[j-1]:
				changes[i][j]=changes[i-1][j-1]
			else:
				changes[i][j]=1+min(min(changes[i-1][j],changes[i][j-1]),changes[i-1][j-1])

	# for i in range(l1+1):
	# 	print(changes[i])

	return changes[l1][l2]


str1 = "azced"
str2 = "abcdef"

print(minimumEditDistance(str1,str2))