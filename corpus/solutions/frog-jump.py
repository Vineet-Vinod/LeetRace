from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable: dict[int, set[int]] = {stone: set() for stone in stones}
        reachable[0].add(0)
        for stone in stones:
            for jump in reachable[stone]:
                for step in (jump - 1, jump, jump + 1):
                    destination = stone + step
                    if step > 0 and destination in reachable:
                        if destination == stones[-1]:
                            return True
                        reachable[destination].add(step)
        return False
