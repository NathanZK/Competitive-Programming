class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        n = 0
        while n < len(nums):
            if nums[n] == 0:
                nums.pop(n)
                count += 1
            else:
                n += 1
        while count > 0:
            nums.append(0)
            count -= 1
