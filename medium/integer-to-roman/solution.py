class Solution:
    def intToRoman(self, num: int) -> str:
        ths = ["", "M", "MM", "MMM"]
        hrns = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (
            ths[num // 1000]
            + hrns[(num % 1000) // 100]
            + tens[(num % 100) // 10]
            + ones[num % 10]
        )
