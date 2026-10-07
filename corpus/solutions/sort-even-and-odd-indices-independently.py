class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[::2])
        odds = sorted(nums[1::2], reverse=True)
        result = nums.copy()
        result[::2] = evens
        result[1::2] = odds
        return result
