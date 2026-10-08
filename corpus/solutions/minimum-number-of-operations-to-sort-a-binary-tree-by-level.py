class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        answer = 0
        queue = deque([root])
        while queue:
            values: list[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            ordered = sorted(values)
            positions = {value: i for i, value in enumerate(ordered)}
            visited = [False] * len(values)
            for i in range(len(values)):
                if visited[i]:
                    continue
                cycle = 0
                current = i
                while not visited[current]:
                    visited[current] = True
                    current = positions[values[current]]
                    cycle += 1
                answer += max(0, cycle - 1)
        return answer
