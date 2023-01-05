class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = (num1[:-1]).split("+")
        num2 = (num2[:-1]).split("+")
        mulComplex = [0, 0]
        mulComplex[0] = int(num1[0]) * int(num2[0]) - (int(num1[1]) * int(num2[1]))
        mulComplex[1] = int(num1[0]) * int(num2[1]) + (int(num1[1]) * int(num2[0]))

        mulComplex = [str(i) for i in mulComplex]
        return "+".join(mulComplex) + "i"
