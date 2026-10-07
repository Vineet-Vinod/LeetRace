from typing import List

Run = tuple[int, str, str, int, int, int]


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        size = 1
        while size < n:
            size *= 2
        tree = [(0, "", "", 0, 0, 0)] * (2 * size)

        def merge(a: Run, b: Run) -> Run:
            if not a[0]:
                return b
            if not b[0]:
                return a
            same = a[2] == b[1]
            prefix = a[3] + (b[3] if same and a[3] == a[0] else 0)
            suffix = b[4] + (a[4] if same and b[4] == b[0] else 0)
            best = max(a[5], b[5], a[4] + b[3] if same else 0)
            return (a[0] + b[0], a[1], b[2], prefix, suffix, best)

        for i, ch in enumerate(s):
            tree[size + i] = (1, ch, ch, 1, 1, 1)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])
        ans = []
        for i, ch in zip(queryIndices, queryCharacters):
            i += size
            tree[i] = (1, ch, ch, 1, 1, 1)
            i //= 2
            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i //= 2
            ans.append(tree[1][5])
        return ans
