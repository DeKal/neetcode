class MinStack:

    def __init__(self):
        self.q = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.q.append(val)
        if not self.min_stack or self.min_stack[-1] >= val:
            self.min_stack.append(val)
        print(self.min_stack)

    def pop(self) -> None:
        
        if self.min_stack and self.min_stack[-1] == self.q[-1]:
            self.min_stack.pop()
        self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def getMin(self) -> int:
     
        return self.min_stack[-1]
