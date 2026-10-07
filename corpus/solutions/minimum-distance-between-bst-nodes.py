class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        previous: int | None = None
        minimum = float("inf")

        def visit(node: Optional[TreeNode]) -> None:
            nonlocal previous, minimum
            if node is None:
                return
            visit(node.left)
            if previous is not None:
                minimum = min(minimum, node.val - previous)
            previous = node.val
            visit(node.right)

        visit(root)
        return int(minimum)
