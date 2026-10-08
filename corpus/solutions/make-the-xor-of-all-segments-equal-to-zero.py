from collections import Counter
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        states = 1 << max(nums).bit_length()
        dp = [len(nums) + 1] * states
        dp[0] = 0
        for start in range(k):
            group = nums[start::k]
            counts = Counter(group)
            baseline = min(dp) + len(group)
            nxt = [baseline] * states
            for value, frequency in counts.items():
                cost = len(group) - frequency
                for xor in range(states):
                    nxt[xor] = min(nxt[xor], dp[xor ^ value] + cost)
            dp = nxt
        return dp[0]
