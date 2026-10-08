class Solution:
    def minimumSteps(self, s: str) -> int:
        black_seen = 0
        swaps = 0
        for ball in s:
            if ball == "1":
                black_seen += 1
            else:
                swaps += black_seen
        return swaps
