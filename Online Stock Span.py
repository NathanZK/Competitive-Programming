class StockSpanner:

    def __init__(self):
        self.dec_stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.dec_stack and price >= self.dec_stack[-1][0]:
            p, c = self.dec_stack.pop()
            count += c

        self.dec_stack.append([price, count])
        return count

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
