class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def prune(node: Optional[TreeNode], total: int) -> Optional[TreeNode]:
            if node is None:
                return None
            total += node.val
            if node.left is None and node.right is None:
                return node if total >= limit else None
            node.left = prune(node.left, total)
            node.right = prune(node.right, total)
            return node if node.left is not None or node.right is not None else None

        return prune(root, 0)
