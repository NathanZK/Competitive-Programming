class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        once = set()

        for c in s:
            if c in once:
                freq[c] -=1
                continue

            while stack and c < stack[-1] and freq[stack[-1]] > 1:
                last = stack.pop()
                freq[last] -= 1
                once.remove(last)

            stack.append(c)
            once.add(c)

        return "".join(stack)

        
