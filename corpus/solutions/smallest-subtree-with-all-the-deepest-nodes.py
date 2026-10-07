class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def visit(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if node is None:
                return 0, None
            left_depth, left_node = visit(node.left)
            right_depth, right_node = visit(node.right)
            if left_depth == right_depth:
                return left_depth + 1, node
            if left_depth > right_depth:
                return left_depth + 1, left_node
            return right_depth + 1, right_node

        return visit(root)[1]
