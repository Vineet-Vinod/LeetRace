class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = sum(value for value in nums if value < 10)
        double = sum(value for value in nums if value >= 10)
        total = single + double
        return single > total - single or double > total - double
