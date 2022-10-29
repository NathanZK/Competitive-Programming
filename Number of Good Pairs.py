class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        res = 0
        for n in count.values():
            res += self.helper(n)
        
        return res
             
    def helper(self, n):
        sum = 0
        for i in range(1, n):
            sum += i
        return sum
