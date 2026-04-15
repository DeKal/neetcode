class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        r = len(grid)
        c = len(grid[0])

        def dfs(i,j):
            grid[i][j] = -1
            res = 1
  
            for x, y in directions:
                ni = x+i
                nj = y+j
                if 0<=ni<r and 0<=nj<c and grid[ni][nj] == 1:
                    res += dfs(ni,nj)
        
            return res

        max_area = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))

        return max_area