class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []
        n = len(s)
        is_palin = [[False] * n for _ in range(n)]

        for length in range(1, n+1):
            for left in range(0, n-length+1):
                right = left+length-1
                is_palin[left][right] = (s[left] == s[right] and (left+1>right-1 or is_palin[left+1][right-1]))


        def dfs(j, i):
            if i == len(s):
                if i == j:
                    res.append(part.copy())
                return

            if is_palin[j][i]:
                part.append(s[j : i + 1])
                dfs(i + 1, i + 1)
                part.pop()

            dfs(j, i + 1)

        dfs(0, 0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

