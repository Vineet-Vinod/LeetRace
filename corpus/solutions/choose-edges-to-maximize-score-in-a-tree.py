class Solution:
    def maxScore(self, edges: List[List[int]]) -> int:
        n = len(edges)
        children: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for node in range(1, n):
            parent, weight = edges[node]
            children[parent].append((node, weight))
        order = [0]
        for node in order:
            order.extend(child for child, _ in children[node])
        free = [0] * n
        blocked = [0] * n
        for node in reversed(order):
            gains = []
            for child, weight in children[node]:
                free[node] += free[child]
                blocked[node] += free[child]
                gains.append(weight + blocked[child] - free[child])
            if gains:
                free[node] += max(0, max(gains))
        return free[0]
