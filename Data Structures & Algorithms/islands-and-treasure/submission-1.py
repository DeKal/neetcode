class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        inf = 2147483647
        visited = [[False] * m for _ in range(n)]

        def dfs(i,j,count):
            grid[i][j] = min(count, grid[i][j])
            for x,y in directions:
                ni = x+i
                nj = y+j
                if 0<=ni<n and 0<=nj<m and grid[ni][nj] != -1 and count<grid[ni][nj] and not visited[ni][nj]:
                    visited[ni][nj] = True
                    dfs(ni, nj, count+1)
                    visited[ni][nj] = False

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dfs(i,j, 0)