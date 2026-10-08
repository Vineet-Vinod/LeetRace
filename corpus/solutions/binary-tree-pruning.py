class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def contains_one(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False
            left_has_one = contains_one(node.left)
            right_has_one = contains_one(node.right)
            if not left_has_one:
                node.left = None
            if not right_has_one:
                node.right = None
            return node.val == 1 or left_has_one or right_has_one

        return root if contains_one(root) else None
