class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix = 0
        low = 0
        high = 0
        for difference in differences:
            prefix += difference
            low = min(low, prefix)
            high = max(high, prefix)
        return max(0, upper - lower - (high - low) + 1)
