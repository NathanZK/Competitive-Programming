class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arrangedSigns = [0 for i in nums]
        pos, neg = 0, 1
        for i in nums:
            if i > 0:
                arrangedSigns[pos] = i
                pos += 2
            else:
                arrangedSigns[neg] = i
                neg += 2
        return arrangedSigns
