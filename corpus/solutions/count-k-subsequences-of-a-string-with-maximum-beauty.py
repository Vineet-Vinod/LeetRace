import builtins
from collections import Counter
from math import comb


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        freq = sorted(Counter(s).values(), reverse=True)
        if k > len(freq):
            return 0
        cutoff = freq[k - 1]
        above = [x for x in freq if x > cutoff]
        need = k - len(above)
        mod = 10**9 + 7
        result = comb(freq.count(cutoff), need) * builtins.pow(cutoff, need, mod) % mod
        for x in above:
            result = result * x % mod
        return result
