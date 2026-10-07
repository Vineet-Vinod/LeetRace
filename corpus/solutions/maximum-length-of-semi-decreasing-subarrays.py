class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        starts: List[int] = []
        maximum = None
        for index, value in enumerate(nums):
            if maximum is None or value > maximum:
                starts.append(index)
                maximum = value
        best = 0
        for end in range(len(nums) - 1, -1, -1):
            while starts and nums[starts[-1]] > nums[end]:
                best = max(best, end - starts.pop() + 1)
        return best
