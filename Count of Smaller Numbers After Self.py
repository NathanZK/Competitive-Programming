class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        
        def mergeSort(start, end):
            if start == end:
                return [start]

            mid = (start+end)//2
            left = mergeSort(start, mid)
            right = mergeSort(mid+1, end)

            return merge(left, right)

        def merge(left, right):
            p1, p2 = 0, 0
            prefix = [0] * (len(left))

            while p1 < len(left) and p2 < len(right):
                if nums[left[p1]] > nums[right[p2]]:
                    prefix[p1] += 1
                    p2 += 1
                else:
                    p1 += 1

            count[left[0]] += prefix[0]
            for i in range(1, len(prefix)):
                prefix[i] += prefix[i-1]
                count[left[i]] += prefix[i]

            p1, p2 = 0, 0
            merged = []
            while p1 < len(left) and p2 < len(right):
                if nums[left[p1]] < nums[right[p2]]:
                    merged.append(left[p1])
                    p1 += 1
                else:
                    merged.append(right[p2])
                    p2 += 1

            merged.extend(left[p1:])
            merged.extend(right[p2:])

            return merged

        mergeSort(0, len(nums)-1)
        return count
                        
