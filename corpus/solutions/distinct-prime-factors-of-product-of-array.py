class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes = set()
        for value in nums:
            divisor = 2
            while divisor * divisor <= value:
                if value % divisor == 0:
                    primes.add(divisor)
                    while value % divisor == 0:
                        value //= divisor
                divisor += 1
            if value > 1:
                primes.add(value)
        return len(primes)
