class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        total = 0
        for start in range(len(s)):
            vowels = 0
            for end in range(start, len(s)):
                if s[end] in "aeiou":
                    vowels += 1
                length = end - start + 1
                if 2 * vowels == length and (vowels * vowels) % k == 0:
                    total += 1
        return total
