class Solution:
    def selfDivisiblePermutationCount(self, n: int) -> int:
        choices = [0] * n
        for position in range(1, n + 1):
            mask = 0
            for value in range(1, n + 1):
                if math.gcd(position, value) == 1:
                    mask |= 1 << (value - 1)
            choices[position - 1] = mask

        @lru_cache(None)
        def count(mask: int) -> int:
            position = mask.bit_count()
            if position == n:
                return 1
            available = choices[position] & ~mask
            total = 0
            while available:
                bit = available & -available
                total += count(mask | bit)
                available ^= bit
            return total

        return count(0)
