class Solution:
    def compress(self, chars: List[str]) -> int:
        left, right = 0, 1
        while right < len(chars):
            while right < len(chars) and chars[left] == chars[right]:
                right += 1

            diff = right - left
            if diff > 1: 
                chars[left + 1: right] = str(diff)
                left += len(str(diff))

            left += 1
            right = left + 1

        return(len(chars))

  
   
