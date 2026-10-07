class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = powers[i - 1] * 2 % (10**9 + 7)
        left, right = 0, len(nums) - 1
        answer = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                answer += powers[right - left]
                left += 1
            else:
                right -= 1
        return answer % (10**9 + 7)
