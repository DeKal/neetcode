class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        n = len(s)
        window = set()
        length = 0
        while r < n:
            if s[r] not in window:
                window.add(s[r])
                length = max(length, len(window))
            else:
                while s[l] != s[r]:
                    if s[l] in window:
                        window.remove(s[l])
                    l+=1
                l+=1
            r+=1
        return length