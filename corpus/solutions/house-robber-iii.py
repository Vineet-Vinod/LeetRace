class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        values: dict[int, tuple[int, int]] = {}
        stack: list[tuple[TreeNode, bool]] = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                left = values.get(id(node.left), (0, 0))
                right = values.get(id(node.right), (0, 0))
                take = node.val + left[1] + right[1]
                skip = max(left) + max(right)
                values[id(node)] = (take, skip)
            else:
                stack.append((node, True))
                if node.right is not None:
                    stack.append((node.right, False))
                if node.left is not None:
                    stack.append((node.left, False))
        return max(values[id(root)])
