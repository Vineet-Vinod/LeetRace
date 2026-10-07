class Solution:
    def heightOfTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        height = 0
        pending = [(root, 0)]
        while pending:
            node, depth = pending.pop()
            height = max(height, depth)

            is_linked_leaf = (
                node.left is not None
                and node.right is not None
                and node.left.right is node
                and node.right.left is node
            )
            if is_linked_leaf:
                continue

            if node.left is not None:
                pending.append((node.left, depth + 1))
            if node.right is not None:
                pending.append((node.right, depth + 1))
        return height
