class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greater = [-1] * len(nums)

        for i in range(len(nums) * 2):
            i = i % len(nums)
            while stack and nums[i] > nums[stack[-1]]:
                ind = stack.pop()
                if greater[ind] == -1:
                    greater[ind] = nums[i]

            stack.append(i)

        return greater
