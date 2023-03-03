class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i, q in enumerate(queries):
            queries[i] = self.freq(q)

        for i, w in enumerate(words):
            words[i] = self.freq(w)

        words.sort()
        numWords = []
        for q in queries:
            left, right = -1, len(words)
            
            while left + 1 < right:
                mid = (left + right) // 2
                if words[mid] <= q:
                    left = mid
                else:
                    right = mid

            numWords.append(len(words) - right)

        return numWords

    def freq(self, string):
        count = Counter(string)
        return count[min(count.keys())]
