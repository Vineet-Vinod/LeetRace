from typing import List


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n, total = len(nums), sum(nums)
        if not any(total * count % n == 0 for count in range(1, n)):
            return False
        transformed = [value * n - total for value in nums]
        middle = n // 2

        def sums(values: List[int]) -> list[tuple[int, int]]:
            result = [(0, 0)]
            for value in values:
                result += [(total + value, count + 1) for total, count in result]
            return result

        left: dict[int, set[int]] = {}
        for value, count in sums(transformed[:middle]):
            left.setdefault(value, set()).add(count)
        for value, count in sums(transformed[middle:]):
            if -value in left and any(0 < count + other < n for other in left[-value]):
                return True
        return False
