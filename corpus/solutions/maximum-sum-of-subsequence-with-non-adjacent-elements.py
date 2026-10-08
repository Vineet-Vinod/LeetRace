from typing import List


class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        size = 1
        while size < n:
            size *= 2
        negative = -(10**30)
        empty = (0, negative, negative, negative)
        tree = [empty] * (2 * size)

        def merge(a, b):
            result = [negative] * 4
            for left in range(2):
                for right in range(2):
                    result[2 * left + right] = max(
                        a[2 * left + x] + b[2 * y + right]
                        for x in range(2)
                        for y in range(2)
                        if not (x and y)
                    )
            return tuple(result)

        for i, value in enumerate(nums):
            tree[size + i] = (0, negative, negative, value)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        answer = 0
        for position, value in queries:
            i = size + position
            tree[i] = (0, negative, negative, value)
            while i > 1:
                i //= 2
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
            answer = (answer + max(tree[1])) % 1000000007
        return answer
