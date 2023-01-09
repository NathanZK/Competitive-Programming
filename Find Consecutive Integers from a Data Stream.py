class DataStream:

    def __init__(self, value: int, k: int):
        self.count = 0
        self.value = value
        self.k = k
        self.d = deque()

    def consec(self, num: int) -> bool:
        self.d.append(num)
        if num == self.value:
            self.count += 1 

        if len(self.d) - 1 == self.k:
            popped = self.d.popleft()
            if popped == self.value:
                self.count -= 1
        
        if self.count == self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
