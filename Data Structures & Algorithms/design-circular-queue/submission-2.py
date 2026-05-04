class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * (k+1)
        self.k = k + 1
        # k = 5 -> 6
        # 1 2 3 4 5 rear6
        self.front = 0
        self.rear = 0
        # self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
       
        self.q[self.rear] = value
        self.rear = (self.rear + 1)% (self.k)
        # self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1)% (self.k)
        # self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1 + self.k) % self.k]

    def isEmpty(self) -> bool:
        return self.front == self.rear
        

    def isFull(self) -> bool:
        return (self.rear+1)%self.k == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()