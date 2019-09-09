# Given a matrix consisting of only zeroes and ones.Cell containing 1 is available for connection and cell with 0 is not. The task is to find how many number of unique connections that can be made with adjacent cells (on all 8 sides).

grid=[[1 ,0 ,0 ,1],[0,1, 1 ,1],[1, 0, 0, 1]]

rows=len(grid)
cols=len(grid[0])

for i in range(rows):
	for j in range(cols):
		if grid[i][j]==1:
			check(i-1,)


https://www.educative.io/collection/page/5668639101419520/5649050225344512/5668600916475904

https://github.com/yangshun/tech-interview-handbook/tree/master/design