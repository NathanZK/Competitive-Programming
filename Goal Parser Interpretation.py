class Solution:
    def interpret(self, command: str) -> str:
        left = 0
        res = []

        while left < len(command):
            if command[left] == "(":
                if command[left + 1] == ")":
                    res.append("o")
                    left += 1
                else:
                    res.append("al")
                    left += 3
            else:
                res += command[left]
            left += 1

        return "".join(res)
