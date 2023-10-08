class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneWeights = sum(stones)
        target = ceil(stoneWeights / 2)
        dp = {}

        def dfs(index, total):
            if total >= target or index == len(stones):
                return abs(total - (stoneWeights - total))

            if (index, total) in dp:
                return dp[(index, total)]

            dp[(index, total)] = min(dfs(index+1, total), dfs(index+1, total+stones[index]))
            return dp[(index, total)]

        return dfs(0, 0)