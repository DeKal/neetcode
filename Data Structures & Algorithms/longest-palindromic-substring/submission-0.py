class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        is_palin = [[False]*n for _ in range(n)]

        # length = 1 (base case)
        for i in range(n):
            is_palin[i][i] = True

        res = ""
        for length in range(1,n+1):
            for l in range(n-length+1):
                r = l + length - 1
                if s[l] == s[r]:
                    if l + 1 < r - 1:
                        is_palin[l][r] = is_palin[l+1][r-1]
                    else:
                        is_palin[l][r] = True
                    if is_palin[l][r]:
                        res = s[l:r+1]

        return res

