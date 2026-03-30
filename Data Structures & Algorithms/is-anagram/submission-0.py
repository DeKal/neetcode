class Solution:

    def toDict(self, s: str):
        d = dict()
        for c in s:
            if c in d:
                d[c] = d[c] + 1
            else:
                d[c] = 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dictS = self.toDict(s)
        dictT = self.toDict(t)

        return dictS == dictT