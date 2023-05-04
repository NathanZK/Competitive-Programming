class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)
        heap = []
        kFrequent = []

        for word, count in wordCount.items():
            heappush(heap, [-count, word])

        while k > 0:
            c, w = heappop(heap)
            kFrequent.append(w)
            k -= 1

        return kFrequent