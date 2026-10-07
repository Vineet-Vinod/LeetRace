class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        counts = [0] * (1 << len(primes))
        counts[0] = 1
        ones = 0
        for value in nums:
            if value == 1:
                ones += 1
                continue
            mask = 0
            valid = True
            for index, prime in enumerate(primes):
                if value % (prime * prime) == 0:
                    valid = False
                    break
                if value % prime == 0:
                    mask |= 1 << index
            if not valid:
                continue
            for previous in range(len(counts) - 1, -1, -1):
                if counts[previous] and previous & mask == 0:
                    counts[previous | mask] = (
                        counts[previous | mask] + counts[previous]
                    ) % (10**9 + 7)
        return (sum(counts) * (2**ones) % (10**9 + 7) - 1) % (10**9 + 7)
