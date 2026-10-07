class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if any(total[char] < k for char in "abc"):
            return -1
        counts = Counter()
        left = 0
        longest_middle = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while any(counts[value] > total[value] - k for value in "abc"):
                counts[s[left]] -= 1
                left += 1
            longest_middle = max(longest_middle, right - left + 1)
        return len(s) - longest_middle
