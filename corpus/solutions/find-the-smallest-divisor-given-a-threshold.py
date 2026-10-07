class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            middle = (low + high) // 2
            if sum((value + middle - 1) // middle for value in nums) <= threshold:
                high = middle
            else:
                low = middle + 1
        return low
