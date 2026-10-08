from __future__ import annotations
from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        end = [0] * (len(nums) + 1)
        parity = answer = 0
        for i, value in enumerate(nums):
            parity ^= end[i]
            if value ^ parity == 0:
                if i + k > len(nums):
                    return -1
                parity ^= 1
                end[i + k] ^= 1
                answer += 1
        return answer
