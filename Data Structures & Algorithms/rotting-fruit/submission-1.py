class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        max_time = 0
        while q:
            
            top_i, top_j, time = q.popleft()
        
            max_time = max(max_time, time)
            for x,y in directions:
                ni = top_i + x
                nj = top_j + y

                if 0<=ni<n and 0<=nj<m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    q.append((ni,nj,time+1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max_time

