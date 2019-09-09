def stockSpan(prices,S):
	n=len(prices)
	stack=[]
	stack.append(0) # Storing index of the first element
	S[0]=1 # Span of the first element is always 1.
	for i in range(1,n):

		while len(stack)>0 and prices[i]>=prices[stack[-1]]:
			stack.pop()

		S[i]=i+1 if len(stack)==0 else i-stack[-1]
		stack.append(i)

	return

prices=[10,4,5,90,120,80]
S=[0 for i in range(len(prices))]

stockSpan(prices,S)
print(S)
