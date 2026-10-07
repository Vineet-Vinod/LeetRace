class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = 0
        max_count = 0
        best = 0
        for right, char in enumerate(s):
            index = ord(char) - 65
            counts[index] += 1
            max_count = max(max_count, counts[index])
            while right - left + 1 - max_count > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
