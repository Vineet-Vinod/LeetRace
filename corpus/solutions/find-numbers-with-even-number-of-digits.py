class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(number)) % 2 == 0 for number in nums)
