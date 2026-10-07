class Solution:
    def minSteps(self, s: str, t: str) -> int:
        first, second = Counter(s), Counter(t)
        return sum(max(0, count - second[char]) for char, count in first.items())
