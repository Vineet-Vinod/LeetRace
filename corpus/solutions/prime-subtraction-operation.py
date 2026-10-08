class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [
            value
            for value in range(2, 1001)
            if all(value % divisor for divisor in range(2, int(value**0.5) + 1))
        ]
        previous = 0
        for value in nums:
            value - previous
            subtraction = 0
            for prime in primes:
                if prime < value and value - prime > previous:
                    subtraction = prime
                elif prime >= value:
                    break
            current = value - subtraction
            if current <= previous:
                return False
            previous = current
        return True
