from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        low, high = 0, sum(batteries) // n
        while low < high:
            middle = (low + high + 1) // 2
            if sum(min(value, middle) for value in batteries) >= middle * n:
                low = middle
            else:
                high = middle - 1
        return low
