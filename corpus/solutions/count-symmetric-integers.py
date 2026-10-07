class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        total = 0
        for value in range(low, high + 1):
            digits = str(value)
            if len(digits) % 2 == 0:
                half = len(digits) // 2
                if sum(map(int, digits[:half])) == sum(map(int, digits[half:])):
                    total += 1
        return total
