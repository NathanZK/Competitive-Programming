class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def choice(left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]

            choice1 = nums[left] - choice(left+1, right)
            choice2 = nums[right] - choice(left, right-1)

            return max(choice1, choice2)

        win =  choice(0, len(nums)-1)
        return win >= 0
