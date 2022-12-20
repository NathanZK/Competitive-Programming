class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        low = len(min(strs, key = len))
        for i in range(low):
            for s in strs:
                if strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res
