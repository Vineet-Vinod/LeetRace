class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            middle = (left + right) // 2
            if arr[middle] < arr[middle + 1]:
                left = middle + 1
            else:
                right = middle
        return left
