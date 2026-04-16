class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)

        for u,v in prerequisites:
            edges[v].append(u)
 
          
        visiting = [False]*numCourses
        
        def dfs(u):
            if visiting[u]:
                return False
             
            children = edges[u]
            if len(children) == 0:
                return True

            visiting[u] = True
            for v in children:
                
                if not dfs(v):
                    return False
            visiting[u] = False
                    
            edges[u] = []
            return True

        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        