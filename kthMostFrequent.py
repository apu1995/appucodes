def kthMostFrequent(strings,k):
	count={}
	for s in strings:
		if s in count:
			count[s]=count[s]+1
		else:
			count[s]=1
	print(count)
	l=list(count.values())
	l.sort()
	count1=sorted(count.items(),key=lambda x:x[1],reverse=True)
	print(count1)
	print(count1[k])
	res=[]
	for c in count:
		if count[c]==l[k]:
			res.append(c)
	return res

l=["a","a","a","b","b","b"]

print(kthMostFrequent(l,0))