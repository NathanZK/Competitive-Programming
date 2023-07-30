class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = Counter(nums)
        lastNum = defaultdict(int)
        heapify(nums)

        while nums:
            n = heappop(nums)
            if count[n]:
                if lastNum[n-1]:
                    lastNum[n] += 1
                    lastNum[n-1] -= 1
                elif count[n+1] and count[n+2]:
                    lastNum[n+2] += 1
                    count[n+1] -= 1
                    count[n+2] -= 1
                else:
                    return False

                count[n] -= 1

        return True