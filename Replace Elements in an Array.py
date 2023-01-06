class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashInd = {}
        for n, num in enumerate(nums):
            hashInd[num] = n

        for op in operations:
            if op[0] in hashInd:
                hashInd[op[1]] = hashInd[op[0]]
                del hashInd[op[0]]
        
        hashInd = {ind: val for val, ind in hashInd.items()}
        replaced = []
        for i in range(len(nums)):
            replaced.append(hashInd[i])
        return replaced
