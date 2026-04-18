class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # N = len(points)
        # adj = {i: [] for i in range(N)}
        # for i in range(N):
        #     x1, y1 = points[i]
        #     for j in range(i + 1, N):
        #         x2, y2 = points[j]
        #         dist = abs(x1 - x2) + abs(y1 - y2)
        #         adj[i].append([dist, j])
        #         adj[j].append([dist, i])

        # res = 0
        # visit = set()
        # minH = [[0, 0]]
        # while len(visit) < N:
        #     cost, i = heapq.heappop(minH)
        #     if i in visit:
        #         continue
        #     res += cost
        #     visit.add(i)
        #     for neiCost, nei in adj[i]:
        #         if nei not in visit:
        #             heapq.heappush(minH, [neiCost, nei])
        # return res

        n, node = len(points), 0
        dist = [100000000] * n
        visit = [False] * n
        edges, res = 0, 0

        while edges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = (abs(points[i][0] - points[node][0]) +
                           abs(points[i][1] - points[node][1]))
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges += 1

        return res