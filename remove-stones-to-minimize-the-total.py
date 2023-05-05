class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapify(piles)

        while k > 0:
            mostStones = heappop(piles)
            mostStones *= -1
            mostStones -= floor(mostStones/2)
            heappush(piles, -mostStones)

            k-=1

        return -sum(piles)