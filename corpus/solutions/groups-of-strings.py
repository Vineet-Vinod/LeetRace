from typing import List


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        masks = [sum(1 << (ord(ch) - 97) for ch in word) for word in words]
        parent = list(range(len(words)))
        size = [1] * len(words)

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        def merge(a, b):
            a, b = find(a), find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]

        exact = {}
        for i, mask in enumerate(masks):
            if mask in exact:
                merge(i, exact[mask])
            else:
                exact[mask] = i
        deleted = {}
        for mask, i in exact.items():
            bits = mask
            while bits:
                bit = bits & -bits
                bits -= bit
                smaller = mask ^ bit
                if smaller in exact:
                    merge(i, exact[smaller])
                if smaller in deleted:
                    merge(i, deleted[smaller])
                else:
                    deleted[smaller] = i
        roots = [i for i in range(len(words)) if find(i) == i]
        return [len(roots), max(size[i] for i in roots)]
