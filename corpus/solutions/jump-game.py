class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        for index, jump in enumerate(nums):
            if index > furthest:
                return False
            furthest = max(furthest, index + jump)
        return True
