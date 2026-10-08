class Solution:
    def canTraverseAllPairs(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False
        parent = list(range(len(nums)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        owners = {}
        for i, value in enumerate(nums):
            p = 2
            while p * p <= value:
                if value % p == 0:
                    if p in owners:
                        parent[find(i)] = find(owners[p])
                    else:
                        owners[p] = i
                    while value % p == 0:
                        value //= p
                p += 1
            if value > 1:
                if value in owners:
                    parent[find(i)] = find(owners[value])
                else:
                    owners[value] = i
        return all(find(i) == find(0) for i in range(len(nums)))
