class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ths = ["", "M", "MM", "MMM"]

        return ths[num // 1000] + hrns[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10]

""" 
Declare the arrays for each possible value
Isolate the number in the thousandths, hundredths, tenths and oneths place
 """