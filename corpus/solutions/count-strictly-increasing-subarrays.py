class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        run = 0
        total = 0
        previous = None
        for value in nums:
            run = run + 1 if previous is not None and previous < value else 1
            total += run
            previous = value
        return total
