class Solution:
    def balancedString(self, s: str) -> int:
        counts = Counter(s)
        required = len(s) // 4
        if all(counts[char] == required for char in "QWER"):
            return 0
        left = 0
        best = len(s)
        for right, char in enumerate(s):
            counts[char] -= 1
            while left <= right and all(counts[item] <= required for item in "QWER"):
                best = min(best, right - left + 1)
                counts[s[left]] += 1
                left += 1
        return best
