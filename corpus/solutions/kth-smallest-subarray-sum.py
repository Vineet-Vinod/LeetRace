class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def count_at_most(limit):
            left = 0
            total = 0
            count = 0
            for right, value in enumerate(nums):
                total += value
                while total > limit:
                    total -= nums[left]
                    left += 1
                count += right - left + 1
            return count

        left = min(nums)
        right = sum(nums)
        while left < right:
            middle = (left + right) // 2
            if count_at_most(middle) >= k:
                right = middle
            else:
                left = middle + 1
        return left
