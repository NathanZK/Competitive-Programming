class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        nums = [str(i) for i in nums]
        for i in range(1, size):
            key = nums[i]
            p = i - 1
            while p >= 0 and (key + nums[p] > nums[p] + key):
                nums[p+1] = nums[p]
                p -= 1
            nums[p+1] = key

        return str(int("".join(nums)))

