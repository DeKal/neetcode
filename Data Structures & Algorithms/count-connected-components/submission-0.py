class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        
        def visit(u):
            vertices = adj[u]
            visited.add(u)
            for v in vertices:
                if v not in visited:
                    visit(v)

        
        count = 0
        for i in range(n):
            if i not in visited:
                count+=1
                visit(i)


        return count