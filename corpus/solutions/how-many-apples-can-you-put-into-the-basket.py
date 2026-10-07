class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        total = 0
        for count, value in enumerate(sorted(weight), 1):
            total += value
            if total > 5000:
                return count - 1
        return len(weight)
