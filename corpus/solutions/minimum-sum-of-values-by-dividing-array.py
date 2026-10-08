class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        states = {(0, -1): 0}
        m = len(andValues)
        for x in nums:
            nxt = {}
            for (group, mask), cost in states.items():
                if group == m:
                    continue
                mask &= x
                target = andValues[group]
                if mask & target != target:
                    continue
                key = (group, mask)
                nxt[key] = min(nxt.get(key, 10**30), cost)
                if mask == target:
                    key = (group + 1, -1)
                    nxt[key] = min(nxt.get(key, 10**30), cost + x)
            states = nxt
        return states.get((m, -1), -1)
