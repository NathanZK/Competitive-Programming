class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dec_stack = []
        min_ = nums[0]

        for n in nums:
            while dec_stack and n > dec_stack[-1][0]:
                dec_stack.pop()

            if dec_stack and n > dec_stack[-1][1] and n < dec_stack[-1][0]:
                return True

            dec_stack.append([n, min_])
            min_ = min(min_, n)

        return False

            


