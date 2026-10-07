class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        width = 2 * k + 1
        if width > n:
            return result
        window = sum(nums[:width])
        result[k] = window // width if window >= 0 else -((-window) // width)
        for right in range(width, n):
            window += nums[right] - nums[right - width]
            result[right - k] = (
                window // width if window >= 0 else -((-window) // width)
            )
        return result
