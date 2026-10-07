class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph: dict[int, list[int]] = {}
        stack = [root]
        while stack:
            node = stack.pop()
            graph.setdefault(node.val, [])
            for child in (node.left, node.right):
                if child is not None:
                    graph[node.val].append(child.val)
                    graph.setdefault(child.val, []).append(node.val)
                    stack.append(child)
        seen = {start}
        queue = deque([(start, 0)])
        minutes = 0
        while queue:
            value, distance = queue.popleft()
            minutes = max(minutes, distance)
            for neighbor in graph[value]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, distance + 1))
        return minutes
