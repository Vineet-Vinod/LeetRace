class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = total = answer = 0
        for right, x in enumerate(nums):
            total += x
            while left <= right and total * (right - left + 1) >= k:
                total -= nums[left]
                left += 1
            answer += right - left + 1
        return answer
