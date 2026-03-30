class Solution:

    def is_eating_valid(self, piles, h, m):
        if m == 0: return False
        cur_hour = 0
        for pile in piles:
            cur_hour += pile//m 
            if pile%m > 0:
                cur_hour += 1

        return cur_hour <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 0

        for pile in piles:
            r = max(r, pile)

        l = 1

        while l<=r:
            m = l + (r-l)//2

            if not self.is_eating_valid(piles, h, m):
                l = m+1
            else:
                r = m-1
        
        if self.is_eating_valid(piles, h, r):
            return r
        else:
            return r+1
