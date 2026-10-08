class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        best = [0] * n
        for index in range(n - 2, -1, -1):
            best[index] = max(
                (next_index - index) * nums[next_index] + best[next_index]
                for next_index in range(index + 1, n)
            )
        return best[0]
