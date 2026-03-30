class Solution:
    def minWindow(self, s: str, t: str) -> str:
        occ = {}
        for ch in t:
            occ[ch] = occ.get(ch,0) + 1
        w = {}
        l = 0
        res = ""
        min_length = math.inf

        need = len(occ)
        have = 0
        for r in range(0, len(s)):
            ch = s[r]
            w[ch] = w.get(ch ,0) + 1
            if ch in occ and w[ch] == occ[ch]:
                have += 1


            while have == need:
                if r-l+1 < min_length:
                    min_length = r-l+1
                    res = s[l:r+1]

                w[s[l]] -= 1
                if s[l] in occ and w[s[l]] < occ[s[l]]:
                    have -= 1
                l += 1

        return res