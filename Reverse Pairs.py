class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        pairs = 0

        def mergeSort(start, end):
            if start == end:
                return [nums[start]]

            mid = (start+end)//2
            leftArr = mergeSort(start, mid)
            rightArr = mergeSort(mid+1, end)

            return merge(leftArr, rightArr)
        
        def merge(arr1, arr2):
            nonlocal pairs

            p1, p2 = 0, 0
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] > 2 * arr2[p2]:
                    pairs += (len(arr1)-p1)
                    p2 += 1
                else:
                    p1 += 1

            merged = []
            p1, p2 = 0, 0
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] < arr2[p2]:
                    merged.append(arr1[p1])
                    p1 += 1
                else:
                    merged.append(arr2[p2])
                    p2 += 1

            merged.extend(arr1[p1:])
            merged.extend(arr2[p2:])

            return merged

        mergeSort(0, len(nums)-1)
        return pairs
