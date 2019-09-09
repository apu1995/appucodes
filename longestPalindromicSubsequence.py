# DP Approach
def longestPalindromicSubsequence(s):
	n=len(s)

	T=[[0 for j in range(n)]for i in range(n)]
	maxLen=1
	for i in range(n):
		T[i][i]=1

	for l in range(2,n+1):
		for i in range(n-l+1):
			j=i+l-1
			if l==2 and s[i]==s[j]:
				T[i][j]=2
			elif s[i]==s[j]:
				T[i][j]=T[i+1][j-1]+2
			else:
				T[i][j]=max(T[i+1][j],T[i][j-1])

	return T[0][n-1]

# Recursive Approach
def longestPalindromicSubsequenceRecursive(s,start,l):
	if l==1:
		return 1
	if l==0:
		return 0

	if s[start]==s[start+l-1]:
		return 2+ longestPalindromicSubsequenceRecursive(s,start+1,l-2)
	else:
		return max(longestPalindromicSubsequenceRecursive(s,start+1,l-1),longestPalindromicSubsequenceRecursive(s,start,l-1))

s="agbdba"
print(longestPalindromicSubsequence(s))
print(longestPalindromicSubsequenceRecursive(s,0,len(s)))


