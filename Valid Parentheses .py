class Solution(object):
    def isValid(self, s):
        stack = collections.deque()
        complement = {"{": "}", "(": ")", "[": "]" }
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                try:
                    temp = stack.pop()
                except:
                    return False
                if not i == complement.get(temp):
                    return False
        return len(stack) == 0
