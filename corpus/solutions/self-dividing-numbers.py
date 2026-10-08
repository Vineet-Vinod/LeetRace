class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for value in range(left, right + 1):
            digits = str(value)
            if all(digit != "0" and value % int(digit) == 0 for digit in digits):
                result.append(value)
        return result
