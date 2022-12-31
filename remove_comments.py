class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        string = "#".join(source)
        newString = ""
        i = 0
        while i < len(string):
            token = string[i:i+2]
            if token == "//":
                i += 2
                while i < len(string) and string[i] != "#":
                    i += 1
            elif token == "/*":
                i += 2
                while string[i:i+2] != "*/":
                    i += 1
                i += 2
            else:
                newString += string[i]
                i += 1
                
        newString = newString.split("#")
        res = []
        for line in newString:
            if line != "":
                res.append(line)
      
        return res
        

       
