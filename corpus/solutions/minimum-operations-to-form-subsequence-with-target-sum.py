from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:
        if sum(nums) < target:
            return -1
        counts = [0] * 32
        for value in nums:
            counts[value.bit_length() - 1] += 1
        answer = 0
        for bit in range(31):
            if target & (1 << bit):
                if not counts[bit]:
                    source = bit + 1
                    while not counts[source]:
                        source += 1
                    while source > bit:
                        counts[source] -= 1
                        counts[source - 1] += 2
                        source -= 1
                        answer += 1
                counts[bit] -= 1
            counts[bit + 1] += counts[bit] // 2
        return answer
