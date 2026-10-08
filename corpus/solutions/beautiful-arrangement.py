class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def count(mask: int) -> int:
            position = mask.bit_count() + 1
            if position > n:
                return 1
            total = 0
            for value in range(1, n + 1):
                bit = 1 << (value - 1)
                if not mask & bit and (value % position == 0 or position % value == 0):
                    total += count(mask | bit)
            return total

        return count(0)
