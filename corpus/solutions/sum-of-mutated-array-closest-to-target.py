class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        low, high = 0, max(arr)
        while low < high:
            middle = (low + high) // 2
            if sum(min(value, middle) for value in arr) < target:
                low = middle + 1
            else:
                high = middle
        candidates = {low, max(0, low - 1)}
        return min(
            candidates,
            key=lambda value: (abs(sum(min(x, value) for x in arr) - target), value),
        )
