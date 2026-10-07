from collections import Counter


class Solution:
    def countPalindromePaths(self, parent: list[int], s: str) -> int:
        children = [[] for _ in parent]
        for i in range(1, len(parent)):
            children[parent[i]].append(i)
        masks = [0] * len(parent)
        order = [0]
        for u in order:
            for v in children[u]:
                masks[v] = masks[u] ^ (1 << (ord(s[v]) - 97))
                order.append(v)
        seen = Counter()
        answer = 0
        for mask in masks:
            answer += seen[mask]
            for b in range(26):
                answer += seen[mask ^ (1 << b)]
            seen[mask] += 1
        return answer
