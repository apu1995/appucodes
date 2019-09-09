def subsetSum(nums,target):
	n=len(nums)
	if n==0:
		return False
	cache=[[False for j in range(target+1)] for i in range(n)]
	for i in range(n):
		cache[i][0]=True
	if nums[0]<=target:
		cache[0][nums[0]]=True

	for i in range(1,n):
		for j in range(1,target+1):
			if j<nums[i]:
				cache[i][j]=cache[i-1][j]
			else:
				cache[i][j]= (cache[i-1][j] or cache[i-1][j-nums[i]])
				# print("cache[i-1][j] ",cache[i-1][j],"cache[i-1][j-nums[i]] ",cache[i-1][j-nums[i]],"nums[i] ",nums[i],"(i,j) ",i,j)

	for i in range(len(cache)):
		print(cache[i])

	return cache[n-1][target]


nums=[2,3,7,8,10]
target=11
print(subsetSum(nums,target))


# [True, False, True, False, False, False, False, False, False, False, False, False]
# [True, False, True, False, False, False, False, False, False, False, False, False]
# [True, False, True, False, False, False, True, False, False, False, False, False]
# [True, True, True, False, False, False, True, True, False, False, False, False]
# [True, True, True, True, True, False, True, True, False, True, True, False]

