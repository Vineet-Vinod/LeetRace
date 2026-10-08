class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def visit(
            node: Optional[TreeNode], parent_even: bool, grandparent_even: bool
        ) -> int:
            if node is None:
                return 0
            total = node.val if grandparent_even else 0
            return (
                total
                + visit(node.left, node.val % 2 == 0, parent_even)
                + visit(node.right, node.val % 2 == 0, parent_even)
            )

        return visit(root, False, False)
