class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_des = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack_des:
            val = min(val, self.stack_des[-1])
        return self.stack_des.append(val)
        
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_des.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if self.stack_des:
            return self.stack_des[-1]
        


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()