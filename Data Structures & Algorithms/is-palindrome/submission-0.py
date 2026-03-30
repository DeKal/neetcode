class Solution:

    def filterAlphaNumeric(self, s:str) -> str:
        res = ""
        s = s.lower()
        for ch in s:
            if ord("a") <= ord(ch) and ord(ch) <= ord("z") or ord("0") <= ord(ch) and ord(ch) <= ord("9"):
                res+=ch
        return res
    
    def isPalindrome(self, s: str) -> bool:
        s = self.filterAlphaNumeric(s)

        n = len(s)
        for i in range(0, n//2):
            if s[i] != s[n-i-1]:
                return False

        return True