class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        children: List[List[int]] = [[] for _ in range(nodes)]
        for node in range(1, nodes):
            children[parent[node]].append(node)
        order = [0]
        for node in order:
            order.extend(children[node])
        subtree_sum = [0] * nodes
        remaining = [0] * nodes
        for node in reversed(order):
            total = value[node]
            count = 1
            for child in children[node]:
                total += subtree_sum[child]
                count += remaining[child]
            if total != 0:
                subtree_sum[node] = total
                remaining[node] = count
        return remaining[0]
