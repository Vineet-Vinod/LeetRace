class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total = 1
        for divisor in range(2, math.isqrt(num) + 1):
            if num % divisor == 0:
                total += divisor
                if divisor * divisor != num:
                    total += num // divisor
        return total == num
