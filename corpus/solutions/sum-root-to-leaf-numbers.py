class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def visit(node: Optional[TreeNode], prefix: int) -> int:
            if node is None:
                return 0
            value = prefix * 10 + node.val
            if node.left is None and node.right is None:
                return value
            return visit(node.left, value) + visit(node.right, value)

        return visit(root, 0)
