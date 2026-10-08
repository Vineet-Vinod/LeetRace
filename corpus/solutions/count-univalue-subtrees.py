class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def visit(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True
            left_matches = visit(node.left)
            right_matches = visit(node.right)
            if (
                left_matches
                and right_matches
                and (node.left is None or node.left.val == node.val)
                and (node.right is None or node.right.val == node.val)
            ):
                self.count += 1
                return True
            return False

        visit(root)
        return self.count
