class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        pairs = 0
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]

        def mergeSort(start, end, nums):
            if start == end:
                return [nums[start]]

            mid = (start+end)//2
            left = mergeSort(start, mid, nums)
            right = mergeSort(mid+1, end, nums)

            return merge(left, right)

        def merge(left, right):
            nonlocal pairs
            
            p1, p2 = 0, 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] - right[p2] <= diff:
                    pairs += (len(right) - p2)
                    p1 += 1
                else:
                    p2 += 1

            merged = []
            p1, p2 = 0, 0

            while p1 < len(left) and p2 < len(right):
                if left[p1] < right[p2]:
                    merged.append(left[p1])
                    p1 += 1
                else:
                    merged.append(right[p2])
                    p2 += 1

            merged.extend(left[p1:])
            merged.extend(right[p2:])

            return merged

        mergeSort(0, len(nums1)-1, nums1)
        return pairs
