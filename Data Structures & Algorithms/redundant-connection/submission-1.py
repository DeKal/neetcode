class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        m = len(edges)+1 
        rank = [1]*(m)
        parent = [i for i in range(m)]


        def find(u):
            par = parent[u]

            while par != parent[par]:
                parent[par] = parent[parent[par]] # skip
                par = parent[par]

            return par


        def union(u,v):
            p1 = find(u)
            p2 = find(v)

            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return True

        
        for u, v in edges:
            if not union(u,v):
                return [u,v]
        
        return []
