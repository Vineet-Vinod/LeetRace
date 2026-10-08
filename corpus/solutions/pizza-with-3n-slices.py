from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        count = len(slices) // 3

        def linear(values: List[int]) -> int:
            previous = [0] + [-(10**9)] * count
            before_previous = previous[:]
            for value in values:
                current = previous[:]
                for chosen in range(1, count + 1):
                    current[chosen] = max(
                        previous[chosen], before_previous[chosen - 1] + value
                    )
                before_previous, previous = previous, current
            return previous[count]

        return max(linear(slices[:-1]), linear(slices[1:]))
