class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        cycles, remainder = divmod(target, total)
        if remainder == 0:
            return cycles * len(nums)
        best = len(nums) + 1
        left = current = 0
        doubled = nums + nums
        for right, value in enumerate(doubled):
            current += value
            while current > remainder and left <= right:
                current -= doubled[left]
                left += 1
            if current == remainder:
                best = min(best, right - left + 1)
        return cycles * len(nums) + best if best <= len(nums) else -1
