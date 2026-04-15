class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        r = len(grid)
        c = len(grid[0])

        def dfs(i, j):
            grid[i][j] = "x"
            for x, y in directions:
                n_i = x+i
                n_j = y+j
                if 0<= n_i<r and 0<=n_j<c and grid[n_i][n_j] == "1":
                    dfs(n_i, n_j)


        count =0

        for i in range(0, r):
            for j in range(0,c):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count+=1
        
        return count