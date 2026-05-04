class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)

        mp = [-1] * (max_val + 1)

        for start, end in intervals:
            mp[start] = max(end, mp[start])  # Remove +1 here

        res = []
        have = -1
        interval_start = -1

        for i in range(len(mp)):
            if mp[i] != -1:
                if interval_start == -1:
                    interval_start = i
                have = max(mp[i], have)  # Remove -1 here

            if have == i:
                res.append([interval_start, have])
                have = -1
                interval_start = -1

        if interval_start != -1:
            res.append([interval_start, have])

        return res