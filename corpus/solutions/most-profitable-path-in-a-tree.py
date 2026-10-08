class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        size = len(amount)
        graph: List[List[int]] = [[] for _ in range(size)]
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)
        parent = [-1] * size
        depth = [0] * size
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    depth[neighbor] = depth[node] + 1
                    order.append(neighbor)
        bob_time = [size + 1] * size
        node = bob
        time = 0
        while node != -1:
            bob_time[node] = time
            node = parent[node]
            time += 1
        best = -(10**30)
        stack = [(0, -1, 0, 0)]
        while stack:
            node, previous, time, income = stack.pop()
            if time < bob_time[node]:
                income += amount[node]
            elif time == bob_time[node]:
                income += amount[node] // 2
            children = [neighbor for neighbor in graph[node] if neighbor != previous]
            if not children:
                best = max(best, income)
            for child in children:
                stack.append((child, node, time + 1, income))
        return best
