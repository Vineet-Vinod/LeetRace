from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        answer = 0
        previous = {}
        for value in nums:
            current = {value: 1}
            for old, count in previous.items():
                new = old & value
                current[new] = current.get(new, 0) + count
            answer += current.get(k, 0)
            previous = current
        return answer
