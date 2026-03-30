class Solution:
   
    def isValidByCol(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(0, col):
            boardSet = set()
            for j in range(0, row):
                numberCh = board[j][i]
                if numberCh != ".":
                    if numberCh not in boardSet:
                        boardSet.add(numberCh) 
                    else:
                        return False
        return True

    def isValidByRow(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for i in range(0, row):
            boardSet = set()
            for j in range(0, col):
                numberCh = board[i][j]
                if numberCh != ".":
                    if numberCh not in boardSet:
                        boardSet.add(numberCh) 
                    else:
                        return False
        return True

    def isValidByArea(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(0, row, 3):
            for j in range (0, col, 3):
                boardSet = set()
                for x in range(0, 3):
                    for y in range (0,3):
                        numberCh = board[i+x][j+y]
                        if numberCh != ".":
                            if numberCh not in boardSet:
                                boardSet.add(numberCh) 
                            else:
                                return False

        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidByCol(board) and self.isValidByRow(board) and self.isValidByArea(board)
