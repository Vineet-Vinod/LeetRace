class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            high = max(nums[-1] - k, nums[i] + k)
            low = min(nums[0] + k, nums[i + 1] - k)
            answer = min(answer, high - low)
        return answer
