class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        M = m - 1
        N = n - 1
        right = m + n - 1
        
        while N >= 0:
            if M >= 0 and nums1[M] >= nums2[N]:
                nums1[right] = nums1[M]
                M -= 1
            else:
                nums1[right] = nums2[N]
                N -= 1
            right -= 1      
        
