class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        res = 0
        for n in count.values():
            if n != 1:
                res += (n*(n-1))//2
        return res
             
    
        
