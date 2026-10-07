class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        small = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        tens = "Zero Ten Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def group(value: int) -> list[str]:
            words = []
            if value >= 100:
                words.extend([small[value // 100], "Hundred"])
                value %= 100
            if value >= 20:
                words.append(tens[value // 10])
                value %= 10
            if value:
                words.append(small[value])
            return words

        words = []
        for divisor, unit in (
            (10**9, "Billion"),
            (10**6, "Million"),
            (1000, "Thousand"),
            (1, ""),
        ):
            value, num = divmod(num, divisor)
            if value:
                words.extend(group(value))
                if unit:
                    words.append(unit)
        return " ".join(words)
