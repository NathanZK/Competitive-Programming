class Solution(object):
    def multiply(self, num1, num2):
        nums = {"1": 1, "2": 2, "3": 3, "4": 4, "5" : 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0 }
        num1L = len(num1)
        num2L = len(num2)
        num_1 = 0
        num_2 = 0
        for i in range(num1L):
            divisor = 10 ** (num1L - 1 - i)
            num_1 += nums.get(num1[i]) * (divisor)

        for i in range(num2L):
            divisor = 10 ** (num2L - 1 - i)
            num_2 += nums.get(num2[i]) * (divisor)

        return str(num_1 * num_2)
