from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for value in stations:
            prefix.append(prefix[-1] + value)
        power = [prefix[min(n, i + r + 1)] - prefix[max(0, i - r)] for i in range(n)]

        def possible(goal: int) -> bool:
            changes = [0] * (n + 1)
            added = used = 0
            for i in range(n):
                added += changes[i]
                need = max(0, goal - power[i] - added)
                used += need
                if used > k:
                    return False
                added += need
                changes[min(n, i + 2 * r + 1)] -= need
            return True

        low, high = min(power), min(power) + k
        while low < high:
            middle = (low + high + 1) // 2
            if possible(middle):
                low = middle
            else:
                high = middle - 1
        return low
