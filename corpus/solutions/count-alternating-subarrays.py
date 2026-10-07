class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        run = 0
        total = 0
        previous = -1
        for value in nums:
            run = run + 1 if value != previous else 1
            total += run
            previous = value
        return total
