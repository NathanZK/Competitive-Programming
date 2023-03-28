class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = list(set(nums))

        def quickSelect(start, end):
            pivot = count[nums[start]]
            write = start + 1

            for read in range(start+1, end+1):
                if count[nums[read]] < pivot:
                    nums[write], nums[read] = nums[read], nums[write]
                    write += 1

            nums[write-1], nums[start] = nums[start], nums[write-1]

            if len(nums) - k == write-1:
                return nums[write-1:]
            elif len(nums) - k < write - 1:
                return quickSelect(start, write-2) 
            else:
                return quickSelect(write, end)

        return quickSelect(0, len(nums)-1)
