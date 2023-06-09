class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        nextDiff = {}

        for num in arr:
            if num in nextDiff:
                if nextDiff[num] == nextDiff.get(num-difference, 0):
                    nextDiff[num] += 1

            nextDiff[num+difference] = max(nextDiff.get(num, 0), nextDiff.get(num+difference,0))

        return max(nextDiff.values())+1