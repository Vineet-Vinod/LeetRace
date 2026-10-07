class Solution:
    def intToRoman(self, num: int) -> str:
        values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        symbols = (
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        )
        result: list[str] = []
        for value, symbol in zip(values, symbols):
            count, num = divmod(num, value)
            result.extend([symbol] * count)
        return "".join(result)
