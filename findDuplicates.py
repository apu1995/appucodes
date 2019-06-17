# Duplicates in array

def findDuplicates(arr):
	n=len(arr)
	track={}
	dups=[]
	for i in range(n):
		if arr[i] in track:
			if track[arr[i]]==1:
				dups.append(arr[i])
				track[arr[i]]=track[arr[i]]+1
		else:
			track[arr[i]]=1

	return dups

def findDuplicatesOptimal(arr):
	res=[]
	for i in range(len(arr)):
		pos=abs(arr[i])-1
		if arr[pos]<0:
			res.append(abs(arr[i]))
			arr[pos]=0
		else:
			arr[pos]=arr[pos]*-1
	return res


arr1=[1, 2, 3]
arr2=[1, 2, 2]
arr3=[3, 3, 3]
arr4=[2, 1, 2, 1]

print(findDuplicates(arr1))
print(findDuplicates(arr2))
print(findDuplicates(arr3))
print(findDuplicates(arr4))
print(findDuplicatesOptimal(arr1))
print(findDuplicatesOptimal(arr2))
print(findDuplicatesOptimal(arr3))
print(findDuplicatesOptimal(arr4))