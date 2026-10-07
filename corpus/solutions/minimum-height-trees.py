class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        neighbors = [set() for _ in range(n)]
        for first, second in edges:
            neighbors[first].add(second)
            neighbors[second].add(first)
        leaves = deque(index for index in range(n) if len(neighbors[index]) == 1)
        remaining = n
        while remaining > 2:
            layer_size = len(leaves)
            remaining -= layer_size
            for _ in range(layer_size):
                leaf = leaves.popleft()
                neighbor = neighbors[leaf].pop()
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    leaves.append(neighbor)
        return sorted(leaves)
