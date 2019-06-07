def MaxCoins(grid):
	row,col=len(grid),len(grid[0])
	for i in range(1,row):
		grid[i][0]=grid[i-1][0]+grid[i][0]
	for j in range(1,col):
		grid[0][j]=grid[0][j-1]+grid[0][j]

	for i in range(1,row):
		for j in range(1,col):
			grid[i][j]=grid[i][j]+max(grid[i][j-1],grid[i-1][j])

	print(grid)

	return grid[row-1][col-1]

grid= [[0,3,1,1],[2,0,0,4],[1,5,3,1]]
print(MaxCoins(grid))