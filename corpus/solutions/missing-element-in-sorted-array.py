class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        def missing_before(index: int) -> int:
            return nums[index] - nums[0] - index

        if k > missing_before(len(nums) - 1):
            return nums[-1] + k - missing_before(len(nums) - 1)
        left, right = 0, len(nums) - 1
        while left < right:
            middle = (left + right) // 2
            if missing_before(middle) < k:
                left = middle + 1
            else:
                right = middle
        previous = left - 1
        return nums[previous] + k - missing_before(previous)
