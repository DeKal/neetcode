class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        l = 0
        r = n - 1

        while l<=r:
            m = l+(r-l)//2

            if intervals[m][0] < newInterval[0]:
                l = m+1
            else:
                r = m-1
        
        intervals.insert(l, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])

        return res






