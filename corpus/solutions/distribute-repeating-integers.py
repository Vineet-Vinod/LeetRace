class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        from collections import Counter
        from functools import lru_cache

        capacities = sorted(Counter(nums).values(), reverse=True)[: len(quantity)]
        orders = sorted(quantity, reverse=True)

        @lru_cache(None)
        def search(i, remaining):
            if i == len(orders):
                return True
            previous = -1
            for j, capacity in enumerate(remaining):
                if capacity < orders[i] or capacity == previous:
                    continue
                previous = capacity
                nxt = list(remaining)
                nxt[j] -= orders[i]
                if search(i + 1, tuple(sorted(nxt, reverse=True))):
                    return True
            return False

        return search(0, tuple(capacities))
