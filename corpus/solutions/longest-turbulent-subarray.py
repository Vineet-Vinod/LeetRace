class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        up = down = best = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up, down = down + 1, 1
            elif arr[i] < arr[i - 1]:
                down, up = up + 1, 1
            else:
                up = down = 1
            best = max(best, up, down)
        return best
