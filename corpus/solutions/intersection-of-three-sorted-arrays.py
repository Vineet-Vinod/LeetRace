class Solution:
    def arraysIntersection(
        self, arr1: list[int], arr2: list[int], arr3: list[int]
    ) -> list[int]:
        return sorted(set(arr1) & set(arr2) & set(arr3))
