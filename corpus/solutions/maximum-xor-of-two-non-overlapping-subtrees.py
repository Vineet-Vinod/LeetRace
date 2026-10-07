from typing import List


class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        parent = [-1] * n
        order = [0]
        for v in order:
            for u in g[v]:
                if u != parent[v]:
                    parent[u] = v
                    order.append(u)
        sums = values[:]
        for v in reversed(order[1:]):
            sums[parent[v]] += sums[v]
        trie = [[-1, -1]]
        bits = max(sums).bit_length()
        count = 0
        best = 0
        stack = [(0, False)]
        while stack:
            v, done = stack.pop()
            x = sums[v]
            if done:
                node = 0
                for b in range(bits - 1, -1, -1):
                    bit = x >> b & 1
                    if trie[node][bit] == -1:
                        trie[node][bit] = len(trie)
                        trie.append([-1, -1])
                    node = trie[node][bit]
                count += 1
            else:
                if count:
                    node = 0
                    score = 0
                    for b in range(bits - 1, -1, -1):
                        bit = x >> b & 1
                        other = trie[node][1 - bit]
                        if other != -1:
                            score |= 1 << b
                            node = other
                        else:
                            node = trie[node][bit]
                    best = max(best, score)
                stack.append((v, True))
                for u in g[v]:
                    if parent[u] == v:
                        stack.append((u, False))
        return best
