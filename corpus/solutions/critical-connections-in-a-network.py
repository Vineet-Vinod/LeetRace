class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        adjacent = [[] for _ in range(n)]
        for a, b in connections:
            adjacent[a].append(b)
            adjacent[b].append(a)
        entered = [-1] * n
        low = [0] * n
        parent = [-1] * n
        entered[0] = low[0] = 0
        clock = 1
        stack = [(0, 0)]
        answer = []
        while stack:
            node, index = stack[-1]
            if index == len(adjacent[node]):
                stack.pop()
                p = parent[node]
                if p != -1:
                    if low[node] > entered[p]:
                        answer.append([min(node, p), max(node, p)])
                    low[p] = min(low[p], low[node])
                continue
            neighbor = adjacent[node][index]
            stack[-1] = (node, index + 1)
            if neighbor == parent[node]:
                continue
            if entered[neighbor] == -1:
                parent[neighbor] = node
                entered[neighbor] = low[neighbor] = clock
                clock += 1
                stack.append((neighbor, 0))
            else:
                low[node] = min(low[node], entered[neighbor])
        return sorted(answer)
