class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for index, value in enumerate(arr):
            if index == value:
                return index
        return -1
