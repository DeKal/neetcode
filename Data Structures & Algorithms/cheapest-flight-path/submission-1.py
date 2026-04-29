class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 2) for _ in range(n)]

        for u, v, cst in flights:
            adj[u].append([v, cst])

        min_cost_heap = [(0, src, 0)]
        dist[src][0] = 0

        while min_cost_heap:

            cost, top_src, stops = heapq.heappop(min_cost_heap)

            if top_src == dst:
                return cost
                
            if stops == k + 1:
                continue

            if cost > dist[top_src][stops]:
                continue

            for v, cost_v in adj[top_src]:
                new_cost = cost + cost_v
                if dist[v][stops+1] > new_cost:
                    dist[v][stops+1] = new_cost
                    heapq.heappush(min_cost_heap, [new_cost, v, stops+1])
        
        return -1

