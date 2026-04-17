class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, t in times:
            edges[u].append([v,t])

        min_heap = [(0, k)]
        visited = set()
        result = 0
        while min_heap:

            cost, top_vert = heapq.heappop(min_heap)
            if top_vert in visited:
                continue
            
            result = cost
            visited.add(top_vert)

            for vert, time in edges[top_vert]:
                if vert not in visited:
                    heapq.heappush(min_heap, [cost+time, vert])

        return result if len(visited) == n else -1
            
        


