class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        validIP = []

        def dfs(index, curr):
            if curr and len(curr[-1]) > 1 and curr[-1][0] == "0":
                return

            if curr and int(curr[-1]) > 255:
                return

            if index == len(s):
                if len(curr) == 4:
                    validIP.append(".".join(curr))
                return

            if len(curr) == 4:
                return

            for i in range(index, min(index+3, len(s))):
                curr.append(s[index:i+1])
                dfs(i+1, curr)
                curr.pop()

        dfs(0, [])
        return validIP
