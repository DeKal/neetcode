class Solution:

    def filterAlphaNumeric(self, s:str) -> str:
        res = ""
        s = s.lower()
        for ch in s:
            if ord("a") <= ord(ch) and ord(ch) <= ord("z") or ord("0") <= ord(ch) and ord(ch) <= ord("9"):
                res+=ch
        return res
    

    def isAlphaNum(self, ch) -> bool:
        return ord("a") <= ord(ch) <= ord("z") or ord("0") <= ord(ch) <= ord("9") or ord("A") <= ord(ch) <= ord("Z")


    def isPalindrome(self, s: str) -> bool:
        # s = self.filterAlphaNumeric(s)

        # n = len(s)
        # for i in range(0, n//2):
        #     if s[i] != s[n-i-1]:
        #         return False

        l = 0
        r = len(s) - 1 

        while l<r:
            while not self.isAlphaNum(s[l]) and l<r:
                l+=1
            while not self.isAlphaNum(s[r]) and r>l:
                r-=1


            if l < r and s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1

        return True