class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indices = defaultdict(list)
        count = 0

        for i in range(len(s)):
            indices[s[i]].append(i)

        for word in words:
            currIdx = -1
            
            for i in range(len(word)):
                if word[i] not in indices:
                    break
                
                arr = indices[word[i]]
                nextIdx = self.binarySearch(currIdx, arr)
                if nextIdx == -1 or nextIdx < currIdx:
                    break

                currIdx = nextIdx
                if i == len(word)-1:
                    count += 1

        return count

    def binarySearch(self, target, arr):
        left, right = -1, len(arr)

        while left + 1 < right:
            mid = (left + right)//2

            if arr[mid] > target:
                right = mid
            else:
                left = mid

        if right == len(arr):
            return -1

        return arr[right]