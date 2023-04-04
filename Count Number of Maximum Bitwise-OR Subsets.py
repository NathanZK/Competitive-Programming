class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        xorHash = {}
        maxXor, count = 0, 0

        for num in nums:
            maxXor |= num

        def dfs(index, xor, curr):
            nonlocal maxXor, count

            if xor == maxXor:
                count += 1
    
            if index == len(nums):
                return 

            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, xor | nums[i], curr)
                curr.pop()
       
        dfs(0, 0, [])
        return count
