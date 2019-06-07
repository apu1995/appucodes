# Number of Hops

def noOfHops(arr):
	n=len(arr)
	if n==0:
		return True
	i=0
	while i<n and arr[i]!=0:
		i=i+arr[i]
		if i==n-1:
			return True

	return False

arr1=[2, 0, 1, 0]
arr2=[3, 5, 0, 1]
arr3=[1, 5, 0, 1]
arr4=[0, 5, 0, 1]

print(noOfHops(arr1))
print(noOfHops(arr2))
print(noOfHops(arr3))
print(noOfHops(arr4))