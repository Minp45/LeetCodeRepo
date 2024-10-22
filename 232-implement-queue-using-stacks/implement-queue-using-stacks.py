class MyQueue:

    def __init__(self):
        self.queue = []
        self.tempHolding = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        temp = self.queue[0]
        for i in range(len(self.queue)-1):
            self.queue[i] = self.queue[i + 1]
        del self.queue[-1]
        return temp

    def peek(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return self.queue == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()