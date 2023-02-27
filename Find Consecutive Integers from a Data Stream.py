class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = deque()
        
    def consec(self, num: int) -> bool:
        self.queue.appendleft(num)
        if len(self.queue) == self.k+1:
            self.queue.pop()

        if num != self.value:
            self.queue = deque()
        
        return len(self.queue) == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
