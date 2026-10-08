class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        run = 0
        total = 0
        for value in nums:
            if value == 0:
                run += 1
                total += run
            else:
                run = 0
        return total
