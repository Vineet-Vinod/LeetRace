class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        moves = 0
        next_value = 0
        for value in nums:
            assigned = max(value, next_value)
            moves += assigned - value
            next_value = assigned + 1
        return moves
