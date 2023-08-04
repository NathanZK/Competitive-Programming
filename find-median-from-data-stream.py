class MedianFinder:

    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        if len(self.heap) % 2 == 0:
            mid = len(self.heap)//2
            return (self.heap[mid] + self.heap[mid - 1])/2
        else:
            return self.heap[len(self.heap)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()