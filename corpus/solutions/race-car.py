from functools import lru_cache


class Solution:
    def racecar(self, target: int) -> int:
        @lru_cache(None)
        def solve(t):
            if t == 0:
                return 0
            bits = t.bit_length()
            if t == (1 << bits) - 1:
                return bits
            answer = bits + 1 + solve((1 << bits) - 1 - t)
            forward = (1 << (bits - 1)) - 1
            for back in range(bits - 1):
                remaining = t - forward + (1 << back) - 1
                answer = min(answer, bits + back + 1 + solve(remaining))
            return answer

        return solve(target)
