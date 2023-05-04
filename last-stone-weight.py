class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-num for num in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            top1 = heapq.heappop(stones)
            top2 = heapq.heappop(stones)
            if abs(top1 - top2):
                heapq.heappush(stones, top1 - top2)
        
        if stones:
            return -heapq.heappop(stones)
        return 0