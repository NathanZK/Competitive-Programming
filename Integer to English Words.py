class Solution(object):
    def numberToWords(self, num):
        oneToNine = ['', ' One',' Two', ' Three',' Four',' Five', ' Six', ' Seven', ' Eight', ' Nine']
        tento19 = [' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        twentyToNinety = ['', '', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        hunToBill = ['', ' Thousand', ' Million', ' Billion']

        number = []
        Word = []
        len = 10
        orgNum = num
        for i in range(len):
            divisor = 10 ** (len - 1 - i)
            number.append(int(num / divisor))
            num %= (divisor)

        Word.append(oneToNine[number[0]])
        Word.append(hunToBill[3]) if number[0] != 0 else ""

        for i in range(1, len, 3):
            Word.append(oneToNine[number[i]])
            Word.append(" Hundred") if number[i] != 0 else ""
            if number[i + 1] == 1:
                Word.append(tento19[number[i + 2]])
            else:
                Word.append(twentyToNinety[number[i + 1]])
                Word.append(oneToNine[number[i + 2]])
            Word.append(hunToBill[2 - int(i/3)]) if number[i + 2] != 0 or number[i + 1] != 0 or number[i] != 0 else ""

        if orgNum == 0:
            Word = "Zero"
        Word = "".join(Word).strip()

        return Word
