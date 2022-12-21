class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(t)
        for i in s:
            if i in count:
                if count[i] == 1:
                    del count[i]
                else:
                    count[i] -= 1
        return list(count)[0]
