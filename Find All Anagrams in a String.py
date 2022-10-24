class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ana = collections.Counter(p)
        n = len(p)
        st = collections.Counter(s[0:n])
        left, right = 0, n - 1
        res = []
        while right < len(s):
            if ana == st:
                res.append(left)
            right += 1
            if right == len(s):
                return res
            
            if st.get(s[left]) == 1:
                st.pop(s[left])
            else:
                st[s[left]] = st.get(s[left]) - 1
            left += 1
            st[s[right]] = st.get(s[right], 0) + 1
