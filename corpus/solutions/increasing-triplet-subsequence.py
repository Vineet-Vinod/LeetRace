class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = second = float("inf")
        for value in nums:
            if value <= first:
                first = value
            elif value <= second:
                second = value
            else:
                return True
        return False
