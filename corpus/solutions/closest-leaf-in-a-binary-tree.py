class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        graph: dict[int, list[int]] = {}
        leaves: set[int] = set()
        stack: list[tuple[TreeNode, Optional[TreeNode]]] = (
            [(root, None)] if root is not None else []
        )
        while stack:
            node, parent = stack.pop()
            graph.setdefault(node.val, [])
            if parent is not None:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            if node.left is None and node.right is None:
                leaves.add(node.val)
            if node.left is not None:
                stack.append((node.left, node))
            if node.right is not None:
                stack.append((node.right, node))
        queue = deque([k])
        visited = {k}
        while queue:
            level = [queue.popleft() for _ in range(len(queue))]
            candidates = [value for value in level if value in leaves]
            if candidates:
                return min(candidates)
            for value in level:
                for neighbor in graph[value]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return k
