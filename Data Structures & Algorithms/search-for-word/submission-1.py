class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
                
        r = len(board)
        c = len(board[0])

        def dfs(i, j, cur_pos): 
            if cur_pos == len(word)-1:
                return True

            tmp = board[i][j]
            board[i][j] = "."
            p = [0, 0, 1, -1]
            q = [1, -1, 0 , 0]

            res = False
            for d in range(0,4):
                nr = i + p[d]
                nc = j+ q[d]
                
                if 0 <= nr < r and 0<=nc<c and board[nr][nc] == word[cur_pos+1]:
                    res = res | dfs(nr,nc, cur_pos+1)
            board[i][j] = tmp
            return res




        for i in range(0, r):
            for j in range (0, c):
                if board[i][j] == word[0]:
                    if dfs(i, j , 0):
                        return True

        return False

  