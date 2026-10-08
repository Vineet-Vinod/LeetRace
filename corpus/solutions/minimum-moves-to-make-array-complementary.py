class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        changes = [0] * (2 * limit + 2)
        for index in range(len(nums) // 2):
            left, right = nums[index], nums[-1 - index]
            low, high = sorted((left, right))
            changes[low + 1] -= 1
            changes[high + limit + 1] += 1
            changes[left + right] -= 1
            changes[left + right + 1] += 1
        best = len(nums)
        moves = len(nums)
        for total in range(2, 2 * limit + 1):
            moves += changes[total]
            best = min(best, moves)
        return best
