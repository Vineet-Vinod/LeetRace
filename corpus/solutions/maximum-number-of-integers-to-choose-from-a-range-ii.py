class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        blocked = sorted(value for value in set(banned) if value <= n)
        count = total = start = 0

        def take_range(first: int, last: int) -> tuple[int, int, bool]:
            available_count = max(0, last - first + 1)
            available_sum = available_count * (first + last) // 2
            if available_sum <= maxSum - total:
                return available_count, available_sum, True
            low, high = 0, available_count
            while low < high:
                middle = (low + high + 1) // 2
                partial_sum = middle * (2 * first + middle - 1) // 2
                if partial_sum <= maxSum - total:
                    low = middle
                else:
                    high = middle - 1
            partial_sum = low * (2 * first + low - 1) // 2
            return low, partial_sum, False

        for value in blocked + [n + 1]:
            added_count, added_sum, complete = take_range(start + 1, value - 1)
            count += added_count
            total += added_sum
            if not complete:
                break
            start = value
        return count
