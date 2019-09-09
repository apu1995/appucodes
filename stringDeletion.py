def stringDeletion(words,query):
	strs=[]
	strSet=set()
	strs.append(query)
	strSet.add(query)

	while len(strs)>0:
		curr=strs.pop(0)
		if curr in words:
			return len(query)-len(curr)
		else:
			for i in range(len(curr)):
				temp=curr[0:i]+curr[i+1:]

				if temp not in strSet and len(temp)>0:
					strs.append(temp)
					strSet.add(temp)
	return -1

words={'a', 'aa', 'aaa'}
query="abc"
print(stringDeletion(words,query))
query="ddd"
print(stringDeletion(words,query))

