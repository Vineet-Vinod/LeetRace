class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        bits = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        first = {0: -1}
        mask = best = 0
        for i, char in enumerate(s):
            mask ^= bits.get(char, 0)
            if mask in first:
                best = max(best, i - first[mask])
            else:
                first[mask] = i
        return best
