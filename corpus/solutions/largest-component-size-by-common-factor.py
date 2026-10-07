from typing import List


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        from collections import Counter

        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        owner = {}
        for i, value in enumerate(nums):
            factor = 2
            factors = []
            while factor * factor <= value:
                if value % factor == 0:
                    factors.append(factor)
                    while value % factor == 0:
                        value //= factor
                factor += 1
            if value > 1:
                factors.append(value)
            for factor in factors:
                if factor in owner:
                    left, right = find(i), find(owner[factor])
                    if left != right:
                        if size[left] < size[right]:
                            left, right = right, left
                        parent[right] = left
                        size[left] += size[right]
                else:
                    owner[factor] = i
        return max(Counter(find(i) for i in range(n)).values())
