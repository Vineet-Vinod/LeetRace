class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        reversed_values = {int(str(value)[::-1]) for value in nums}
        return len(set(nums) | reversed_values)
