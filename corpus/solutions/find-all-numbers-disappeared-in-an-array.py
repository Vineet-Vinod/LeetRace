class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [value for value in range(1, len(nums) + 1) if value not in present]
