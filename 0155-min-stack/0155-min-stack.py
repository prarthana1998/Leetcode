class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, val: int) -> None:
        if not self.stack:
            curr_min = val
        else:
            curr_min = min(val, self.stack[-1][1])
        return self.stack.append((val, curr_min))
        
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()