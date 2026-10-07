class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def at_most(bound: int) -> int:
            total = run = 0
            for x in nums:
                run = run + 1 if x <= bound else 0
                total += run
            return total

        return at_most(right) - at_most(left - 1)
