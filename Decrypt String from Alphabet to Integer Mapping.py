class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {}
        char = 'a'
        
        while char <= 'z':
            hashmap[str(ord(char) - 96)] = char
            char = chr(ord(char) + 1)
            
        stack = list(s)
        res = []
        while stack:
            last = stack.pop()
            if last == '#':
                sec = stack.pop()
                first = stack.pop()
                res.append(hashmap[first + sec])
            else:
                res.append(hashmap[last])

        return "".join(res[::-1])
