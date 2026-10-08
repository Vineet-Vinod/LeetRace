class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            if sum(value >= x for value in nums) == x:
                return x
        return -1
