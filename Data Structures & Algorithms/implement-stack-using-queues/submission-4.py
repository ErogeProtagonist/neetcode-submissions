class MyStack:
    def __init__(self):
        self.queue_1 = deque([])
    def push(self, x: int) -> None:
        self.queue_1.append(x)

    def pop(self) -> int:
        holder = deque([])
        for i in range(len(self.queue_1)-1):
            holder.append(self.queue_1.popleft())
        value = self.queue_1.popleft()
        self.queue_1 = holder
        return value

    def top(self) -> int:
        holder = deque([])
        for i in range(len(self.queue_1)-1):
            holder.append(self.queue_1.popleft())
        value = self.queue_1[0]
        holder.append(self.queue_1.popleft())
        self.queue_1 = holder
        
        
        return value
        

    def empty(self) -> bool:
        return not self.queue_1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()