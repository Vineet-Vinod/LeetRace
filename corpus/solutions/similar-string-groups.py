from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        words = list(set(strs))
        parent = list(range(len(words)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i, a in enumerate(words):
            for j in range(i):
                if find(i) == find(j):
                    continue
                mismatches = 0
                for x, y in zip(a, words[j]):
                    if x != y:
                        mismatches += 1
                        if mismatches > 2:
                            break
                if mismatches <= 2:
                    parent[find(i)] = find(j)
        return len({find(i) for i in range(len(words))})
