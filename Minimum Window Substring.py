class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        setLet = set(t)
        extra = {}
        left, minLength, window = 0, float("inf"), ""

        for right in range(len(s)):
            if s[right] in setLet:
                if s[right] not in count:
                    extra[s[right]] = extra.get(s[right], 0) + 1
                else:
                    count[s[right]] -= 1
                    if count[s[right]] == 0:
                        del count[s[right]]

            while len(count) == 0:
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    window = s[left:right+1]

                if s[left] in extra:
                    extra[s[left]] -= 1
                    if extra[s[left]] == 0:
                        del extra[s[left]]

                elif s[left] in setLet:
                    count[s[left]] = count.get(s[left], 0) + 1

                left += 1

        return window

            
