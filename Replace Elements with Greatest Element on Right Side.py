class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        replaced = [0] * len(arr)
        replaced[-1] = -1
        max_ = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            replaced[i] = max_
            max_ = max(max_, arr[i])
            
        return replaced
            
        
