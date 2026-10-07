class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        positive_start = nums[0]
        negative_start = -(10**30)
        answer = positive_start
        for value in nums[1:]:
            positive_start, negative_start = (
                max(value, negative_start + value),
                positive_start - value,
            )
            answer = max(answer, positive_start, negative_start)
        return answer
