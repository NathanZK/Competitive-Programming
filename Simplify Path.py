class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for c in path:
            if stack and c == "..":
                stack.pop()
            elif c != "" and c != ".." and c != ".":
                stack.append(c)

        return "/"+ "/".join(stack)
