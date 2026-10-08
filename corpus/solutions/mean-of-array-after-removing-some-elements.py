class Solution:
    def trimMean(self, arr: List[int]) -> float:
        values = sorted(arr)
        trim = len(values) // 20
        return sum(values[trim : len(values) - trim]) / (len(values) - 2 * trim)
