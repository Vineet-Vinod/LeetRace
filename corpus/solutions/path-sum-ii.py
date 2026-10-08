class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        paths: list[list[int]] = []
        path: list[int] = []
        stack = [(root, 0, False)]
        while stack:
            node, parent_sum, exiting = stack.pop()
            if exiting:
                path.pop()
                continue
            path.append(node.val)
            total = parent_sum + node.val
            if node.left is None and node.right is None:
                if total == targetSum:
                    paths.append(path.copy())
                path.pop()
                continue
            stack.append((node, total, True))
            if node.right is not None:
                stack.append((node.right, total, False))
            if node.left is not None:
                stack.append((node.left, total, False))
        return sorted(paths)
