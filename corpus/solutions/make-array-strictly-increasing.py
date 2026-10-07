from bisect import bisect_right


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        choices = sorted(set(arr2))
        states = {-1: 0}
        for x in arr1:
            nxt = {}
            for last, cost in states.items():
                if x > last:
                    nxt[x] = min(nxt.get(x, 10**9), cost)
                j = bisect_right(choices, last)
                if j < len(choices):
                    y = choices[j]
                    nxt[y] = min(nxt.get(y, 10**9), cost + 1)
            states = {}
            best = 10**9
            for last, cost in sorted(nxt.items()):
                if cost < best:
                    states[last] = cost
                    best = cost
            if not states:
                return -1
        return min(states.values())
