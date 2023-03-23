class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quickSelect(start, end):
            pivot = nums[start]
            write = start + 1

            for read in range(start+1, end+1):
                if nums[read] < pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1

            nums[write-1], nums[start] = nums[start], nums[write-1]

            if len(nums) - k == write-1:
                return nums[write-1]
            elif len(nums) - k > write - 1:
                return quickSelect(write, end)
            else:
                return quickSelect(start, write-2)
            

        return quickSelect(0, len(nums)-1)
       
