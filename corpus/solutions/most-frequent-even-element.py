class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter

        counts = Counter(value for value in nums if value % 2 == 0)
        return min(counts, key=lambda value: (-counts[value], value)) if counts else -1
