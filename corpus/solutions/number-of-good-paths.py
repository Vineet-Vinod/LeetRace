from collections import Counter, defaultdict
from typing import List


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        adjacency = [[] for _ in range(n)]
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)
        parent = list(range(n))
        size = [1] * n

        def find(i):
            while parent[i] != i:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i

        groups = defaultdict(list)
        for i, value in enumerate(vals):
            groups[value].append(i)
        answer = 0
        for value, nodes in sorted(groups.items()):
            for u in nodes:
                for v in adjacency[u]:
                    if vals[v] <= value:
                        a, b = find(u), find(v)
                        if a != b:
                            if size[a] < size[b]:
                                a, b = b, a
                            parent[b] = a
                            size[a] += size[b]
            counts = Counter(find(u) for u in nodes)
            answer += sum(count * (count + 1) // 2 for count in counts.values())
        return answer
