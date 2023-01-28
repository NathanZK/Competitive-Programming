class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targetIndices = []
        nums.sort()
        for index, num in enumerate(nums):
            if num == target:
                targetIndices.append(index)

        return targetIndices
