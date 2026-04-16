class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        in_degrees = defaultdict(int)

        for u,v in prerequisites:
            edges[v].append(u)
            in_degrees[u] += 1

        print(in_degrees)
        q = deque([])
        for c in range(numCourses):
            if c not in in_degrees:
                q.append(c)

        done = 0
        while q:
            u = q.popleft()
            done += 1

            nexts = edges[u]
            for v in nexts:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    q.append(v)
        print(done)
        return done == numCourses
                
 
          
        # visiting = [False]*numCourses
        
        # def dfs(u):
        #     if visiting[u]:
        #         return False
             
        #     children = edges[u]
        #     if len(children) == 0:
        #         return True

        #     visiting[u] = True
        #     for v in children:
                
        #         if not dfs(v):
        #             return False
        #     visiting[u] = False
                    
        #     edges[u] = []
        #     return True

        
        # for c in range(numCourses):
        #     if not dfs(c):
        #         return False
        # return True


        