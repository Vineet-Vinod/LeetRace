class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        columns = defaultdict(list)
        queue = deque([(root, 0)])
        minimum = maximum = 0
        while queue:
            node, column = queue.popleft()
            columns[column].append(node.val)
            minimum = min(minimum, column)
            maximum = max(maximum, column)
            if node.left is not None:
                queue.append((node.left, column - 1))
            if node.right is not None:
                queue.append((node.right, column + 1))
        return [columns[column] for column in range(minimum, maximum + 1)]
