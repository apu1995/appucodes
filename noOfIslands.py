# Number of Island Clusters


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        if rows==0:
            return 0
        cols=len(grid[0])
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    count=count+1
                    dfs(i,j,grid)
        return count

def dfs(i,j,grid):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0':
        return
    grid[i][j]='0'
    dfs(i-1,j,grid)
    dfs(i,j-1,grid)
    dfs(i+1,j,grid)
    dfs(i,j+1,grid)