class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(value for value, count in Counter(nums).items() if count == 1)
