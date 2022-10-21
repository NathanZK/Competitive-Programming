class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = []
        for m in range (1,n+1):
            if m%5==0 and m%3==0:
                arr.append("FizzBuzz")
            elif m%3==0:
                arr.append("Fizz")
            elif m%5==0:
                arr.append("Buzz")
            else:
                arr.append(str(m))
        return arr
