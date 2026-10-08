from typing import List


class Solution:
    def maxGeneticDifference(
        self, parents: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(parents)
        children = [[] for _ in parents]
        root = 0
        for i, parent in enumerate(parents):
            if parent == -1:
                root = i
            else:
                children[parent].append(i)
        by_node = [[] for _ in parents]
        for i, (node, value) in enumerate(queries):
            by_node[node].append((i, value))
        trie = [[-1, -1, 0]]
        bits = max(n, 200000).bit_length()

        def change(value, delta):
            at = 0
            trie[at][2] += delta
            for bit in range(bits - 1, -1, -1):
                direction = (value >> bit) & 1
                if trie[at][direction] == -1:
                    trie[at][direction] = len(trie)
                    trie.append([-1, -1, 0])
                at = trie[at][direction]
                trie[at][2] += delta

        answer = [0] * len(queries)
        stack = [(root, 1)]
        while stack:
            node, delta = stack.pop()
            change(node, delta)
            if delta == -1:
                continue
            for i, value in by_node[node]:
                at, result = 0, 0
                for bit in range(bits - 1, -1, -1):
                    direction = (value >> bit) & 1
                    other = trie[at][1 - direction]
                    if other != -1 and trie[other][2]:
                        at = other
                        result |= 1 << bit
                    else:
                        at = trie[at][direction]
                answer[i] = result
            stack.append((node, -1))
            stack.extend((child, 1) for child in children[node])
        return answer
