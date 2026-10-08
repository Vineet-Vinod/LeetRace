class Solution:
    def numSplits(self, s: str) -> int:
        right_counts = Counter(s)
        left_chars = set()
        good = 0
        for char in s[:-1]:
            left_chars.add(char)
            right_counts[char] -= 1
            if right_counts[char] == 0:
                del right_counts[char]
            if len(left_chars) == len(right_counts):
                good += 1
        return good
