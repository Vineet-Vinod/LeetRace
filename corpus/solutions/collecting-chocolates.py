class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        best = nums[:]
        answer = sum(best)
        for rotations in range(1, n):
            for kind in range(n):
                best[kind] = min(best[kind], nums[(kind - rotations) % n])
            answer = min(answer, sum(best) + rotations * x)
        return answer
