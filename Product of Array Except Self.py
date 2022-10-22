class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, postfix = [1] * n, [1] * n
        result = []
        i = 1
        while i < n:
            prefix[i] = prefix[i - 1] * nums[i - 1]
            i += 1
        i -= 1
        while i > 0:
            postfix[i - 1] = postfix[i] * nums[i]
            i -= 1
        for i in range(n):
            result.append(prefix[i] * postfix[i])
        return result
