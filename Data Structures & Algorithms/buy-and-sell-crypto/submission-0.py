class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1 
        n = len(prices)
        maxP = 0
        while r < n:
            if prices[l] < prices[r]:
                maxP = max(maxP, prices[r] - prices[l])
                r+=1
            else:
                l = r
                r = l+1

        return maxP
