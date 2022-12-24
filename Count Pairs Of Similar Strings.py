class Solution:
    def similarPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            words[i] = set(words[i])
            words[i] = "".join(sorted(words[i]))

        hashmap = Counter(words)
        count = 0
        for val in hashmap.values():
            count += ((val) * (val - 1))/2

        return int(count)
