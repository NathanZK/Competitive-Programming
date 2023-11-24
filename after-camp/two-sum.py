class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashMap:
                return [i, hashMap[complement]]

            hashMap[num] = i
        