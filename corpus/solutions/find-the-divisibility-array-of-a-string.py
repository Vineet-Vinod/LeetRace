class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        remainder = 0
        result = []
        for digit in word:
            remainder = (remainder * 10 + int(digit)) % m
            result.append(int(remainder == 0))
        return result
