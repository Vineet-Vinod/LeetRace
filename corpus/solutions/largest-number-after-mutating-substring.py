class Solution:
    def maximumNumber(self, num: str, change: list[int]) -> str:
        digits = list(num)
        started = False
        for index, digit in enumerate(num):
            mapped = str(change[int(digit)])
            if mapped > digit:
                started = True
                digits[index] = mapped
            elif mapped == digit and started:
                digits[index] = mapped
            elif started:
                break
        return "".join(digits)
