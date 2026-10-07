class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        return sum(all(abs(value - other) > d for other in arr2) for value in arr1)
