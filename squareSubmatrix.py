# Square Submatrix

def squareSubmatrix(arr):
	rows=len(arr)
	if rows==0:
		return 0
	cols=len(arr[0])
	cache=[[0 for _ in range(cols)] for _ in range(rows)]
	maxSize=0
	for i in range(rows):
		if arr[i][0]==1:
			cache[i][0]=1
			maxSize=1

	for j in range(cols):
		if arr[0][j]==1:
			cache[0][j]=1
			maxSize=1
	
	for i in range(1,rows):
		for j in range(1,cols):
			if arr[i][j]==1:
				cache[i][j]=min(min(cache[i-1][j],cache[i][j-1]),cache[i-1][j-1])+1
			if cache[i][j]>maxSize:
				maxSize=cache[i][j]

	return maxSize


arr=[[0, 1, 1, 0],[1, 1, 1, 1],[1, 1, 1, 0]]
print(squareSubmatrix(arr))