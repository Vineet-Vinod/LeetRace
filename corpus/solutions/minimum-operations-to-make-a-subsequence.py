from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        from bisect import bisect_left

        positions = {value: i for i, value in enumerate(target)}
        tails: list[int] = []
        for value in arr:
            if value not in positions:
                continue
            index = positions[value]
            place = bisect_left(tails, index)
            if place == len(tails):
                tails.append(index)
            else:
                tails[place] = index
        return len(target) - len(tails)
