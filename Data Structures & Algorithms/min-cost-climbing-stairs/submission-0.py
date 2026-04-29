class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        min_cost = [10000000]*(n)
        min_cost[0] = cost[0]
        min_cost[1] = cost[1]

        for i in range(2, n):
            min_cost[i] = min(min_cost[i-1]+ cost[i], min_cost[i-2] + cost[i])

        return min_cost[-1]