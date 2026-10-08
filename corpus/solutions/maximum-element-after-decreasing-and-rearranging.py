class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        maximum = 0
        for value in arr:
            maximum = min(maximum + 1, value)
        return maximum
