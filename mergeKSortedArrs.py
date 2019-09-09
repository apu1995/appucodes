def mergeKSortedArr(arrs,beg=0,end=0):
	k=len(arr)
	end=k
	while(beg<end):
		mid=int(beg+end/2)
		merge(arr)
	

def merge(arr1,arr2):
	len1=len(arr1)
	len2=len(arr2)
	temp=[]
	while i<len1 and j<len2:
		if arr1[i]<arr2[j]:
			temp.append(arr1[i])
			i=i+1
		else:
			temp.append(arr2[j])
			j=j+1
	if i<len1:
		while i<len1:
			temp.append(arr1[i])
			i=i+1

	if j<len2:
		while j<len2:
			temp.append(arr2[j])
			j=j+1

	return temp



arrs=[[1, 4, 7],[2, 5, 8],[3, 6, 9]]