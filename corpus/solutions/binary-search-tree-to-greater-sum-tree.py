class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running_sum = 0

        def visit(node: Optional[TreeNode]) -> None:
            nonlocal running_sum
            if node is None:
                return
            visit(node.right)
            running_sum += node.val
            node.val = running_sum
            visit(node.left)

        visit(root)
        return root
