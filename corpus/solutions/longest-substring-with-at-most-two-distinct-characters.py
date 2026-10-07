class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts: dict[str, int] = {}
        left = best = 0
        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            while len(counts) > 2:
                old = s[left]
                counts[old] -= 1
                if counts[old] == 0:
                    del counts[old]
                left += 1
            best = max(best, right - left + 1)
        return best
