from __future__ import annotations
from typing import List


class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in nums]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        parent = [-1] * n
        order = [0]
        for a in order:
            for b in adj[a]:
                if b != parent[a]:
                    parent[b] = a
                    order.append(b)
        total = sum(nums)
        for count in range(n, 1, -1):
            if total % count:
                continue
            target = total // count
            if target < max(nums):
                continue
            sums = nums[:]
            valid = True
            for a in reversed(order):
                if sums[a] > target:
                    valid = False
                    break
                if sums[a] != target and parent[a] != -1:
                    sums[parent[a]] += sums[a]
            if valid and sums[0] == target:
                return count - 1
        return 0
