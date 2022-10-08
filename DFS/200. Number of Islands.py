class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        def dfs(grid, i, j):
            if grid[i][j]=="0": # stop 시점
                return
            grid[i][j] = "0"
            if i < len(grid)-1:
                dfs(grid, i+1, j)
            if i-1 >= 0:
                dfs(grid, i-1, j)
            if j < len(grid[i])-1:
                dfs(grid, i, j+1)
            if j-1 >= 0:
                dfs(grid, i, j-1)
        
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    cnt += 1
        return cnt
