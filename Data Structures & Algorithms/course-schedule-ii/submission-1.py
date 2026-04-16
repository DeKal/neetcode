class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        in_degrees = defaultdict(int)

        for u,v in prerequisites:
            edges[v].append(u)
            in_degrees[u] += 1

        
        q = deque([])
        for c in range(numCourses):
            if c not in in_degrees:
                q.append(c)
                
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            nexts = edges[u]
            for v in nexts:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    q.append(v)
        
        return res if len(res) == numCourses else []