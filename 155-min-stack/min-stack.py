class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.minStack and self.minStack[-1] == top:
            self.minStack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] if self.minStack else None


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()