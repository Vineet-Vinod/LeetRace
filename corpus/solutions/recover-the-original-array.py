from typing import List
from collections import Counter


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        values = sorted(nums)
        for difference in sorted(
            {
                x - values[0]
                for x in values
                if x > values[0] and (x - values[0]) % 2 == 0
            }
        ):
            counts = Counter(values)
            result = []
            for x in values:
                if not counts[x]:
                    continue
                if not counts[x + difference]:
                    break
                counts[x] -= 1
                counts[x + difference] -= 1
                result.append(x + difference // 2)
            else:
                return result
        return []
