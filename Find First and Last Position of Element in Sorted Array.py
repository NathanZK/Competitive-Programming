class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        return [first, last]

    def findFirst(self, nums, target):
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if right != len(nums) and nums[right] == target:
            return right

        return -1

    def findLast(self, nums, target):
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if left != -1 and nums[left] == target:
            return left

        return -1
