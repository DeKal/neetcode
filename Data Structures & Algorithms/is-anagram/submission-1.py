class Solution:

    def toDict(self, s: str):
        d = dict()
        for c in s:
            d[c] = d.get(c, 0) + 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictS = self.toDict(s)
        dictT = self.toDict(t)

        return dictS == dictT