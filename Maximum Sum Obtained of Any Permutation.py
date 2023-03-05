class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        req = [0] * (len(nums)+1)
        hashReq = {}

        for start, end in requests:
            req[start] += 1
            req[end+1] -= 1

        for i in range(1, len(req)):
            req[i] += req[i-1]

        for ind in range(len(req)-1):
            hashReq[ind] = req[ind]

        hashReq = sorted(hashReq.items(), key = lambda x: x[1], reverse = True)

        for i in range(len(hashReq)):
            req[hashReq[i][0]+1] = nums[i]

        req[0] = 0
        for i in range(1, len(req)):
            req[i] += req[i-1]

        totalSum = 0
        for start, end in requests:
            totalSum += (req[end+1] - req[start])

        return (totalSum % (10**9 + 7))


        
