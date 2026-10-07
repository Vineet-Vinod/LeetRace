class Solution:
    def minSteps(self, s: str, t: str) -> int:
        differences = Counter(s)
        differences.subtract(t)
        return sum(abs(count) for count in differences.values())
