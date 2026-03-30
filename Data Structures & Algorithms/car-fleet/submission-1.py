class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        time = [0]*n

        for i in range(0,n):
            time[i] = (position[i], (target-position[i])/speed[i])

        time.sort()


        stack = deque([time[0][1]])
        for i in range(1, n):
            actual_time = time[i][1]

            while stack and actual_time >= stack[-1]:
                stack.pop()
            stack.append(actual_time)

    
        return len(stack)