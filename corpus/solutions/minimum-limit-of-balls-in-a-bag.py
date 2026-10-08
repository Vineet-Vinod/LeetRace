class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            limit = (left + right) // 2
            operations = sum((balls - 1) // limit for balls in nums)
            if operations <= maxOperations:
                right = limit
            else:
                left = limit + 1
        return left
