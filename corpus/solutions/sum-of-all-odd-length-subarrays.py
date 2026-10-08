class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        size = len(arr)
        for index, value in enumerate(arr):
            occurrences = (index + 1) * (size - index)
            total += ((occurrences + 1) // 2) * value
        return total
