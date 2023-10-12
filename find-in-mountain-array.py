# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        length = mountain_arr.length()

        left, right = -1, length
        while left + 1 < right:
            mid = (left + right)//2
            if mid == 0:
                left = mid
                continue

            currVal = mountain_arr.get(mid)
            prevVal = mountain_arr.get(mid-1)

            if currVal > prevVal:
                left = mid
            else:
                right = mid

        currVal = mountain_arr.get(left)
        if currVal < target:
            return -1

        elif currVal == target:
            return left
        
        currInd = left
        left, right = 0, currInd + 1

        while left + 1 < right:
            mid = (left + right)//2
            currVal = mountain_arr.get(mid)

            if currVal > target:
                right = mid
            else:
                left = mid

        if left != -1 and mountain_arr.get(left) == target:
            return left

        left, right = currInd, length
        while left + 1 < right:
            mid = (left + right)//2
            currVal = mountain_arr.get(mid)

            if currVal < target:
                right = mid
            else:
                left = mid

        if left != -1 and mountain_arr.get(left) == target:
            return left

        return -1