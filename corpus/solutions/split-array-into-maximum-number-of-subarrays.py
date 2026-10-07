class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        total = nums[0]
        for value in nums[1:]:
            total &= value
        if total:
            return 1
        answer = 0
        current = (1 << 31) - 1
        for value in nums:
            current &= value
            if current == 0:
                answer += 1
                current = (1 << 31) - 1
        return answer
