class Solution:
    def decodeString(self, s: str) -> str:
        return self.decode(s, 0)[0]

    def decode(self, s, index):
        res = ""

        while index < len(s) and s[index] != "]":
            if s[index].isdigit():
                num = "0"
                while index < len(s) and s[index].isdigit():
                    num += s[index]
                    index += 1

                index += 1
                sub_str, index = self.decode(s, index)
                res += int(num) * sub_str

            else:
                res += s[index]
                index += 1

        return res, index + 1

