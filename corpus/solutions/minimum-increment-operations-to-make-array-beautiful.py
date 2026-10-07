class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = {0: 0}
        for index, value in enumerate(nums):
            cost = max(0, k - value)
            next_dp = {}
            for mask, total in dp.items():
                for chosen in (0, 1):
                    if index >= 2 and mask == 0 and chosen == 0:
                        continue
                    new_mask = ((mask << 1) | chosen) & 3
                    candidate = total + (cost if chosen else 0)
                    next_dp[new_mask] = min(next_dp.get(new_mask, 10**30), candidate)
            dp = next_dp
        return min(dp.values())
