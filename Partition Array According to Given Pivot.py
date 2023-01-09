class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before, after = [], []
        pivotCount = 0
        for n in nums:
            if n < pivot:
                before.append(n)
            elif n == pivot:
                pivotCount += 1
            else:
                after.append(n)

        return before + [pivot] * pivotCount + after
        
