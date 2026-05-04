class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 2 -> 3 
        # 1 2 3
        # 4 5 6
        # 7 8 9

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):

                # save top-left
                # l , l +i
                topLeft = matrix[l][l + i]

                # bottom-left → top-left

                # r-i, l
                matrix[l][l + i] = matrix[r - i][l]

                # bottom-right → bottom-left
                # r, r-i
                matrix[r - i][l] = matrix[r][r - i]

                # top-right → bottom-right
                # l+i, r
                matrix[r][r - i] = matrix[l + i][r]

                # top-left → top-right
                matrix[l + i][r] = topLeft

            r -= 1
            l += 1