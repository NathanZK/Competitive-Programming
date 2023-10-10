class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = self.isIPv4(queryIP)
        if ipv4:
            return "IPv4"

        ipv6 = self.isIPv6(queryIP)
        if ipv6:
            return "IPv6"

        return "Neither"

    def isIPv4(self, queryIP):
        arr = queryIP.split(".")
        if len(arr) != 4:
            return False

        for num in arr:
            if len(num) < 1:
                return False
                
            if num[0] == "0" and len(num) > 1:
                return False
            
            if not num.isdigit():
                return False

            if int(num) < 0 or int(num) > 255:
                return False

        return True

    def isIPv6(self, queryIP):
        arr = queryIP.split(":")
        if len(arr) != 8:
            return False

        hexaDecimals = {"a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"}
        for num in arr:
            if len(num) < 1 or len(num) > 4:
                return False

            for n in num:
                if not n.isdigit() and n not in hexaDecimals:
                    return False

        return True