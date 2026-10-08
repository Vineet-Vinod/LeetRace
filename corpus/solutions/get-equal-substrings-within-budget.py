class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cost = 0
        longest = 0
        for right, (first, second) in enumerate(zip(s, t)):
            cost += abs(ord(first) - ord(second))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            longest = max(longest, right - left + 1)
        return longest
