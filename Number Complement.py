class Solution:
    def findComplement(self, num: int) -> int:
        max_ = math.ceil(math.log2(num))
        if num == 2**(max_):
            return 2**(max_) - 1

        mask = 2**(max_) - 1
        return num ^ mask
