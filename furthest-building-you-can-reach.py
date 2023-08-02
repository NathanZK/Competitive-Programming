class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        furthest = 0

        for i in range(1, len(heights)):
            diff = heights[i]-heights[i-1]
            if diff > 0 and ladders > 0:
                ladders -= 1
                heappush(heap, diff)
            elif diff > 0 and ladders == 0:
                heappush(heap, diff)
                minDiff = heappop(heap)
                if minDiff <= bricks:
                    bricks -= minDiff
                else:
                    return i - 1
            
            furthest = i

        return furthest