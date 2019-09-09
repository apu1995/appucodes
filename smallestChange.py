def smallesChange(x):
	coins=[10,5,2,1]
	minChange=0
	for coin in coins:
		currChange=x//coin
		x=x-(currChange*coin)
		minChange=minChange+currChange

	return minChange

print(smallesChange(10))
print(smallesChange(11))
print(smallesChange(23))
print(smallesChange(25))
print(smallesChange(9))