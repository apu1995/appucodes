# Maximum number of partitions that can be sorted individually to make sorted

def maxPartitions(arr):
	n=len(arr)
	if n==0:
		return 0
	maxsofar=0
	count=0
	for i in range(n):
		maxsofar=max(maxsofar,arr[i])
		if maxsofar==i:
			count=count+1

	return count


arr=[2, 1, 0, 3, 4, 5]
print(maxPartitions(arr))

