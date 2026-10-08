class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        best = 0
        for distinct_limit in range(1, 27):
            counts = [0] * 26
            left = unique = enough = 0
            for right, char in enumerate(s):
                index = ord(char) - ord("a")
                if counts[index] == 0:
                    unique += 1
                counts[index] += 1
                if counts[index] == k:
                    enough += 1
                while unique > distinct_limit:
                    old = ord(s[left]) - ord("a")
                    if counts[old] == k:
                        enough -= 1
                    counts[old] -= 1
                    if counts[old] == 0:
                        unique -= 1
                    left += 1
                if unique == distinct_limit and unique == enough:
                    best = max(best, right - left + 1)
        return best
