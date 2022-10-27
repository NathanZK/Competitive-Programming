class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hashmap = {}
        temp = sorted(nums)
        result = [0] * len(nums)
        for ind, num in enumerate(temp):
            if num not in hashmap:
                hashmap[num] = ind
        for ind, num in enumerate(nums):
            result[ind] = hashmap[num]
        return result
