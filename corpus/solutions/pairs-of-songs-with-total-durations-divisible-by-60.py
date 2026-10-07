class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counts = [0] * 60
        pairs = 0
        for duration in time:
            remainder = duration % 60
            pairs += counts[-remainder % 60]
            counts[remainder] += 1
        return pairs
