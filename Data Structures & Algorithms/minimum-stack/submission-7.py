class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = [2**31]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val <= self.minimum[-1]:
            self.minimum.append(val)
            
    def pop(self) -> None:
        if self.stack[-1] == self.minimum[-1]:
            self.minimum.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
        
