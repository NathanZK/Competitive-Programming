class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        size = len(nums)
        for n in range(size):
            reverse = int(str(nums[n])[::-1])
            nums.append(reverse)

        return (len(set(nums)))
