class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        while n % 2 == 0:
            n //= 2
        answer = 1
        divisor = 3
        while divisor * divisor <= n:
            exponent = 0
            while n % divisor == 0:
                n //= divisor
                exponent += 1
            answer *= exponent + 1
            divisor += 2
        return answer * (2 if n > 1 else 1)
